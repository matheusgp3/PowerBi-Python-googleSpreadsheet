import os.path
from pandas import DataFrame
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class gPlanilhas():

    def __init__(self):
        self.creds = None
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    def authPlanilhas(self):
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

    def authWithToken(self,path='./token.json'):
        try:
            self.creds = Credentials.from_authorized_user_file(path, self.SCOPES)
        except:
            self.authPlanilhas()


    def getValues(self,SPREADSHEET_ID,RANGE_NAME):

        try:
            service = build('sheets', 'v4', credentials=self.creds)

        # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
            else:
                return self.tranformToDataframe(values)

        except HttpError as err:
            print(err)

    def tranformToDataframe(self,ls):
        cols = ls[0]
        rows = ls[1:]

        return DataFrame(rows,columns=cols)

    def main(self,SPREADSHEET_ID,RANGE_NAME):
        self.authWithToken()
        df = self.getValues(SPREADSHEET_ID,RANGE_NAME)
        
        print(df)
        return df

