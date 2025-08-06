from google_auth_oauthlib.flow import InstalledAppFlow
import os.path
from google.auth.transport.requests import Request
import pickle
import json

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.readonly"
]

def get_gmail_service():
    creds = None
    # Check if we already have token.json
    if os.path.exists("token.json"):
        with open("token.json", "r") as token:
            creds_data = json.load(token)
            from google.oauth2.credentials import Credentials
            creds = Credentials.from_authorized_user_info(creds_data, SCOPES)

    # If no creds or expired, log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    from googleapiclient.discovery import build
    return build("gmail", "v1", credentials=creds)

if __name__ == "__main__":
    service = get_gmail_service()
    print("Gmail service authenticated successfully!")
