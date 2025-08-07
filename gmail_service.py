import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from config import SCOPES, CREDENTIALS_FILE, TOKEN_FILE

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']

def authenticate_gmail():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    from googleapiclient.discovery import build
    service = build('gmail', 'v1', credentials=creds)
    return service

def list_messages(service, query, max_results):
    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX'],
        q=query,
        maxResults=max_results
    ).execute()
    messages = results.get('messages', [])
    return messages

def get_message(service, msg_id):
    message = service.users().messages().get(
        userId='me',
        id=msg_id,
        format='full'
    ).execute()
    return message

def modify_message(service, msg_id, add_labels=None, remove_labels=None):
    print("add labels: ", add_labels)
    body = {}
    if add_labels:
        body['addLabelIds'] = add_labels
    if remove_labels:
        body['removeLabelIds'] = remove_labels
    return service.users().messages().modify(
        userId='me',
        id=msg_id,
        body=body
    ).execute()

def list_labels(service):
    results = service.users().labels().list(userId='me').execute()
    return results.get('labels', [])
