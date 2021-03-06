from __future__ import print_function
import pickle
import exceptions as e
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def connect():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(os.path.dirname(__file__) + '/token.pickle'):
        with open(os.path.dirname(__file__) + '/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    else:
        print('Token not found')

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(os.path.dirname(__file__) +
                                                                 '/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except FileNotFoundError:
                raise e.APICredentialsNotFound

        # Save the credentials for the next run
        with open(os.path.dirname(__file__) + '/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service
