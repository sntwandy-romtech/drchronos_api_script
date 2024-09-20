import requests
import json
import time
import random
import os
from dotenv import load_dotenv

# Set the URL and Bearer token
BASE_URL =  os.getenv("BASE_URL_PATIENTS")  # Replace with your actual URL
TOKEN = os.getenv("BEARER_TOKEN")  # Replace with your actual token

# Define a list of common User-Agent strings
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
]

# Function to get patient data
def get_patient_data(session, patient_id):
    url = f"{BASE_URL}{patient_id}?verbose=true"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "User-Agent": random.choice(USER_AGENTS),  # Rotate User-Agent for each request
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract required fields
        patient_info = {
            "id": data.get("id"),
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "date_of_birth": data.get("date_of_birth")
        }
        return patient_info
    else:
        print(f"Error fetching data for patient ID {patient_id}: {response.status_code}")
        return None

# Read the patient IDs from the .txt file
def read_patient_ids(file_path):
    with open(file_path, 'r') as file:
        ids = file.read().split(',')
        ids = [id.strip() for id in ids]  # Clean up whitespace/newline characters
    return ids

# Main function to fetch data and save it to a .json file
def save_patient_data_to_json(file_path):
    patient_ids = read_patient_ids(file_path)
    patient_data = []
    total_ids = len(patient_ids)

    print(f"Total IDs to process: {total_ids}")

    # Create a persistent session
    session = requests.Session()

    for index, patient_id in enumerate(patient_ids, start=1):
        data = get_patient_data(session, patient_id)
        if data:
            patient_data.append(data)

        # Print real-time progress
        print(f"Requested {index}/{total_ids} IDs")

        # Introduce a random delay between 5 to 10 seconds
        delay = random.uniform(5, 10)
        print(f"Waiting for {round(delay, 2)} seconds before the next request...")
        time.sleep(delay)

    # Save the data to a JSON file
    with open('data/patient_data.json', 'w') as json_file:
        json.dump(patient_data, json_file, indent=4)

# Run the function with your file path
file_path = 'data/patients_with_flag_cardiac.txt'  # Replace with your .txt file path
save_patient_data_to_json(file_path)
