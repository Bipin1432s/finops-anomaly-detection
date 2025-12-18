const API_URL = "https://mn11vl35dd.execute-api.us-east-1.amazonaws.com/prod/run";

function runAnalysis() {
    document.getElementById("result").innerHTML = "Running analysis...";

    fetch(API_URL)
        .then(res => {
            if (!res.ok) {
                throw new Error("HTTP error " + res.status);
            }
            return res.json();
        })
        .then(data => {
            document.getElementById("result").innerHTML = `
                <b>Status:</b> Success<br>
                <b>Anomaly Detected:</b> ${data.anomaly_detected}<br>
                <b>Today Cost:</b> ${data.today_cost}<br>
                <b>Average Cost:</b> ${data.average_cost}<br>
                <b>Increase %:</b> ${data.increase_percent}
            `;
        })
        .catch(err => {
            document.getElementById("result").innerHTML =
                "Error running analysis. Check console.";
            console.error(err);
        });
}