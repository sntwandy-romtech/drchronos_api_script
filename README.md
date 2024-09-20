# drchronos_api_script

This repository contains a Python-based solution to automate the extraction of patient data from the DrChrono API. The script retrieves and processes patient information, such as names, IDs, and birth dates, for cardiac data research purposes. It leverages the DrChrono API to pull comprehensive patient data, making it easier to integrate this data into medical research workflows.

###Features:
-Fetches patient data via DrChrono's API with detailed fields such as id, first_name, last_name, and date_of_birth.
-Uses a .txt file containing patient IDs to perform bulk requests.
-Implements a secure approach by using environment variables (via .env) to store sensitive data like the API bearer token.
-Includes functionality to save the retrieved data into a structured JSON file.
-Includes safeguards like randomized delays between API requests to avoid detection and ensure compliance with rate limits.

###Setup:
-Clone this repository.
-Install the required dependencies.
-Set up your environment variables, including the DrChrono API base URL and bearer token.
-Run the Python script to pull and save patient data for further analysis.
