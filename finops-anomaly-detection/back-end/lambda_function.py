import json
import boto3
from datetime import datetime
from decimal import Decimal

# AWS clients
sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = 'Finops_Anomalies'
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:171675361218:finops-alerts'
THRESHOLD_PERCENT = 30

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):

    # Simulated historical costs
    historical_costs = [180, 190, 185, 195, 200, 190, 185]
    today_cost = 320

    avg_cost = sum(historical_costs) / len(historical_costs)
    increase_percent = ((today_cost - avg_cost) / avg_cost) * 100
    anomaly_detected = increase_percent > THRESHOLD_PERCENT

    # Convert all numbers to Decimal
    record = {
        'date': str(datetime.utcnow().date()),
        'today_cost': Decimal(str(round(today_cost, 2))),
        'average_cost': Decimal(str(round(avg_cost, 2))),
        'increase_percent': Decimal(str(round(increase_percent, 2))),
        'anomaly_detected': str(anomaly_detected),
        'source': 'SIMULATED'
    }

    # Store in DynamoDB
    table.put_item(Item=record)

    # Send alert if anomaly detected
    if anomaly_detected:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='FinOps Cost Anomaly Alert',
            Message=(
                f"FinOps Cost Anomaly Detected\n\n"
                f"Today Cost: ${today_cost:.2f}\n"
                f"Average Cost: ${avg_cost:.2f}\n"
                f"Increase: {increase_percent:.2f}%"
            )
        )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "content-type",
            "Access-Control-Allow-Methods": "GET,OPTIONS",
            "content-type": "application/json"
        },
        "body": json.dumps({
            "date": record["date"],
            "today_cost": float(record["today_cost"]),
            "average_cost": float(record["average_cost"]),
            "increase_percent": float(record["increase_percent"]),
            "anomaly_detected": anomaly_detected
        })
    }