# DrChrono Patient Data Pull for Cardiac Research

This repository contains a Python-based solution to automate the extraction of patient data from the DrChrono API. The script retrieves and processes patient information, such as names, IDs, and birth dates, for cardiac data research purposes. It leverages the DrChrono API to pull comprehensive patient data, making it easier to integrate this data into medical research workflows.

## Features:
- Fetches patient data via DrChrono's API with detailed fields such as `id`, `first_name`, `last_name`, and `date_of_birth`.
- Uses a `.txt` file containing patient IDs to perform bulk requests.
- Implements a secure approach by using environment variables (via `.env`) to store sensitive data like the API bearer token.
- Includes functionality to save the retrieved data into a structured JSON file.
- Includes safeguards like randomized delays between API requests to avoid detection and ensure compliance with rate limits.

## Setup:
1. **Clone this repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    ```

2. **Install the required dependencies**:
    Make sure you have Python and pip installed. Then, install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables**:
    Create a `.env` file in the root directory with your DrChrono API base URL and bearer token. Example:
    ```
    BASE_URL_PATIENTS=https://app.drchrono.com/api/patients
    BEARER_TOKEN=your_actual_bearer_token_here
    ```

4. **Run the script**:
    Use the following command to pull patient data:
    ```bash
    python drchrono_getPatients.py
    ```

5. **View output**:
    The patient data will be saved in a structured JSON file (`patient_data.json`) for further analysis.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
