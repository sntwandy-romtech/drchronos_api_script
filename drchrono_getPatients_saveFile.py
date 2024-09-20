import requests
import json
import os
from dotenv import load_dotenv

# Define the initial API endpoint
url = f"{os.getenv('BASE_URL_PATIENTS')}?verbose=true"

# Your actual token should replace 'your_actual_bearer_token' below
bearer_token = os.getenv("BEARER_TOKEN")

# Define the headers, ensuring the correct token format
headers = {'Authorization': f'Bearer {bearer_token}'}

# Initialize a list to store filtered patients with the specified flag
patients_with_flag_cardiac = []

# Function to get patients from the API and handle pagination
def get_all_patients(url):
    total_analyzed = 0  # Initialize the count of analyzed patients
    total_filtered = 0  # Initialize the count of filtered patients
    file_path = "patients_with_flag_cardiac.txt"  # File to store patient data in real-time

    # Open the file in append mode, so it updates in real-time
    with open(file_path, 'a') as f:  # Use 'a' mode to append data to the file
        while url:  # Continue as long as there's a next page
            print(f"Requesting data from: {url}")  # Log the current URL
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                results = data['results']  # Extract patients from the current page
                total_analyzed += len(results)  # Update total count of patients analyzed

                # Filter patients with 'patient_flags' containing id = CARDIAC_FLAG_ID
                for patient in results:
                    patient_flags = patient.get('patient_flags', [])
                    for flag in patient_flags:
                        if flag.get('id') == os.getenv("CARDIAC_FLAG_ID"):
                            patient_id = patient['id']
                            patients_with_flag_cardiac.append(patient_id)
                            total_filtered += 1

                            # Write the patient ID to the file
                            f.write(f"{patient_id},\n")  # Write each patient ID on a new line

                            # Ensure the data is written to the file immediately
                            f.flush()

                            break  # No need to check other flags once we find the match

                print(f"Total patients analyzed so far: {total_analyzed}, Patients filtered: {total_filtered}")  # Print the current counts

                url = data.get('next')  # Get the next page URL if available
                if url:  # If there's a next page, log the transition
                    print(f"Moving to the next page: {url}")
            else:
                print(f"Failed to retrieve patients: {response.status_code}")
                print(response.text)
                break  # Exit if the request fails

# Call the function to get all patients and filter them in real-time
get_all_patients(url)

print(f"Patients with flag ID % Cardiac: {len(patients_with_flag_cardiac)}" % (os.getenv("CARDIAC_FLAG_ID")))
