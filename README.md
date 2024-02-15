# gemini_invoice_reader

https://github.com/heispv/gemini_invoice_reader/assets/102462222/78afaf35-cf9b-4f32-b55c-0748968ff7b3

## README: How to Use This Repository

This repository provides a guide on how to set up and use Google Vertex AI with Gemini Pro API, particularly if you're in the regions which don't have access to the `https://makersuite.google.com/app/` to use Gemini API and Google AI Studio. We'll guide you through the steps necessary to get started.

## Prerequisites

Before you begin, make sure you have the following prerequisites in place:

- A Google Cloud Console account.
- Python 3.10 or higher is installed on your machine.
- Conda is installed for managing virtual environments.

## Clone This Repository
```bash
git clone https://github.com/heispv/gemini_invoice_reader.git
```

## Setting Up Google Cloud Console

1. Visit the [Google Cloud Console](https://console.cloud.google.com/) and log in with your Google account.

2. Navigate to **API & Services** and search for **Vertext AI API** and activate it.

3. Go to **IAM & Admin > Service Accounts** and click on **Create Service Account**.

4. Give your service account a name, and then assign it the roles:
   - "Vertex AI Administrator"
   - "Storage Object Admin"

5. Generate a key for this service account in JSON format. Download the JSON file containing your key credentials.

## Setting Up a Virtual Environment

We recommend using a virtual environment to manage your project dependencies. Here's how to set up a virtual environment using Conda and install the required packages:

1. Create a virtual environment with Python 3.10:
   ```bash
   conda create -p .venv python==3.10 -y
   ```

2. Activate the virtual environment:
   ```bash
   conda activate .venv/
   ```

3. Install the required packages from the `requirements.txt` file:
   ```bash
   pip3 install -r requirements.txt
   ```

## Setting Environment Variables

Before running your code, you need to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your JSON key file:

in the .env file paste the text below
```bash
GOOGLE_APPLICATION_CREDENTIALS="path/to/your/key.json"
```

Replace `"path/to/your/key.json"` with the actual path to your downloaded JSON key file.

also add this variable manually into your system.

## Installing and Initializing Google Cloud SDK

Now, let's set up the Google Cloud SDK on your local machine:

Follow the instructions at [Google Cloud SDK Installation](https://cloud.google.com/sdk/docs/install) and [Initializing and Authorizing the gcloud CLI](https://cloud.google.com/sdk/docs/initializing) to install the Google Cloud SDK and initialize it based on you Service Account which you created in the previous step.


Now you're all set up to use Google Vertex AI with Gemini Pro API!

## Run The Application with Streamlit

Go to your terminal and run the code below:
```bash
streamlit run app.py
```

If you have any questions or encounter issues, feel free to reach out for assistance. Happy coding!
