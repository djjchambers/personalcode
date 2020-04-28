from google_authorisation import Auth

scope = ['https://www.googleapis.com/auth/drive']
local_creds_path = 'C:/Users/djjch/tc_creds/'

# instantiate auth here, returns 'service'
# where service = build('drive', 'v3', credentials=creds)
# using the credentials.json file locally stored
authInst = Auth(scope, local_creds_path)
# todo figure out where to instantiate this auth class - use a helper function? If another module will call this one, need to enclose it
driveservice = authInst.start_service_object()


def get_google_drive_files(service):
    # Call the Drive v3 API
    print("started get_google_files")
    # method is .files.list
    results = service.files().list(fields="nextPageToken, files(id, name)").execute()
    # .get called on service.files().list() with arguments
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

# using service as an argument here, could setup service in enclosing scope
# and just pass one argument to upload_file_to_google_drive, since there is only one "service"
# def upload_file_to_google_drive(service, noteobject):
#
#
# def download_file_from_google_drive():
#     ---