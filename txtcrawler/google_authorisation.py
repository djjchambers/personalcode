import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Auth:
    def __init__(self, scopes, creds_path):
        self.scopes = scopes
        self.creds_path = creds_path
        print("instantiating auth")

    def get_credentials(self):
        print("starting get_credentials function")
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        # todo can I refactor this not to use token.pickle?
        # todo Just return creds from credentials.json in given folder?
        # todo collect all this functionality into class DriveClient?g
        local_pickle = os.path.join(self.creds_path, 'token.pickle')
        if os.path.exists(local_pickle):
            print('found token pickle at', self.creds_path)
            with open(local_pickle, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            print("token not found")
            if creds and creds.expired and creds.refresh_token:
                print('Need to refresh token')
                creds.refresh(Request())
            else:
                # otherwise use available credentials in local folder
                local_creds = os.path.join(self.creds_path, 'credentials.json')
                flow = InstalledAppFlow.from_client_secrets_file(local_creds, self.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(local_pickle, 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def start_service_object(self):
        creds = self.get_credentials()
        service = build('drive', 'v3', credentials=creds)
        return service