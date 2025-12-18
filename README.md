# FinOps Anomaly Detection – Serverless AWS Web Application

## Project Overview
The **FinOps Anomaly Detection** project is a serverless cloud-based web application built on AWS to identify abnormal increases in cloud costs and notify stakeholders. The solution follows **FinOps principles** by enabling cost visibility, anomaly detection, and proactive alerting using a scalable, cost-efficient serverless architecture.

The application provides a web dashboard where users can trigger cost analysis. The backend evaluates cost patterns, detects anomalies using threshold-based logic, stores results for auditing, and sends alert notifications when anomalies are detected.

---

## Problem Statement
Organizations using cloud services often experience unexpected cost spikes due to misconfigurations, unused resources, or sudden workload increases. Without continuous monitoring, these anomalies can lead to budget overruns and inefficient cloud spending.

This project aims to:
- Detect abnormal cost behavior
- Alert users in near real-time
- Provide visibility into cost trends
- Support FinOps cost optimization practices

---

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Cloud Services:** AWS  
- **Compute:** AWS Lambda  
- **API Management:** Amazon API Gateway  
- **Storage:** Amazon S3 (Static Website Hosting)  
- **Database:** Amazon DynamoDB  
- **Notifications:** Amazon SNS (Email Alerts)  
- **Monitoring:** Amazon CloudWatch  
- **CDN & Security:** Amazon CloudFront (HTTPS)

---

## System Architecture
The application follows a fully serverless architecture:

User (Browser)
↓
Amazon CloudFront (HTTPS)
↓
Amazon S3 (Static Website)
↓
Amazon API Gateway (/run)
↓
AWS Lambda (FinOps Anomaly Logic)
├── Amazon DynamoDB (Store Results)
├── Amazon SNS (Send Alerts)
└── Amazon CloudWatch (Logs & Monitoring)

---

## Application Workflow
1. User accesses the web dashboard via CloudFront.
2. Frontend assets are served from Amazon S3.
3. User clicks **Run Cost Analysis**.
4. A request is sent to Amazon API Gateway.
5. API Gateway invokes the AWS Lambda function.
6. Lambda performs anomaly detection logic.
7. Results are stored in Amazon DynamoDB.
8. If an anomaly is detected, an email alert is sent via Amazon SNS.
9. Execution logs are captured in Amazon CloudWatch.

---

## Anomaly Detection Logic
- Uses historical cost data (simulated for demo stability).
- Calculates the average daily cost.
- Compares today’s cost with the historical average.
- Flags an anomaly if the percentage increase exceeds a predefined threshold (30%).

---

## Data Stored in DynamoDB
Each analysis record includes:
- Date
- Today’s cost
- Average historical cost
- Percentage increase
- Anomaly status (True/False)
- Data source

---

## Alerting Mechanism
- Alerts are sent via **Amazon SNS (Email)**.
- Triggered only when an anomaly exceeds the threshold.
- Includes cost details and percentage increase.

---

## Security & Cost Optimization
- HTTPS enabled using Amazon CloudFront.
- Fully serverless (no EC2 instances).
- AWS Free Tier friendly.
- No AWS WAF enabled to avoid unnecessary costs.
- IAM roles follow the principle of least privilege.

---

## Future Enhancements
- Integrate real-time AWS billing data using Cost Explorer
- Add charts and visual analytics
- Implement authentication using Amazon Cognito
- Extend anomaly logic using statistical models (Z-score, moving average)
- Multi-service cost breakdown

---

## Learning Outcomes
- Designed and deployed a complete serverless web application
- Gained hands-on experience with AWS core services
- Implemented FinOps principles for cost monitoring
- Learned real-world challenges like CORS, HTTPS, and IAM permissions

---

## Author
**Bipin Banala**  
Final Year Student | Cloud & Data Enthusiast  

---

## License
This project is intended for educational and learning purposes.

