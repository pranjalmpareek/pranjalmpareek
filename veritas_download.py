import requests

url = "http://localhost:5000/veritas/api/download/"

payload = {
    "start_date": "2025-05-28",
    "end_date": "2025-06-04"
}
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Save the CSV data to a file
    with open("data.csv", "wb") as file:
        file.write(response.content)
    print("CSV file saved as 'data.csv'")
else:
    print(f"Failed to download CSV: {response.status_code}")
