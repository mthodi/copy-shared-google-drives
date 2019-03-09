#!/usr/bin/env python3

from __future__ import print_function
import pickle
import os.path
# import urllib
import argparse
import sys
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
# Scopes are access writes to your Google drive. 
SCOPES = ['https://www.googleapis.com/auth/drive']


def usage():
    """Copies shared files to another folder in drive.
    """
    parser = argparse.ArgumentParser(
        prog="copy_shared_folders",
        description="Copies shared Google Drive Folders",
        usage=' %(prog) s -i FILE_CONTAINING_LIST_OF_SHARED_FOLDER_IDs -c CONFIG_FILE')
    parser.add_argument("-i", help="File containing a list of shared folders/file IDs", type=str)
    parser.add_argument("-c", help="Configuration file. See documentation", type=str)
    return parser

def copy_files(input_list, dest_folder):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # read file IDs
    f_handle = open(input_list, 'r')
    file_IDs = f_handle.readlines()
    count = 1
    folder_id = dest_folder
    
    for file_ID in file_IDs:
        # Retrieve the existing parents to remove
        file_id = file_ID.splitlines()[0]
        # file = service.files().get(fileId=file_id, fields='parents').execute()
        # previous_parents = ",".join(file.get('parents'))
        # Move the file to the new folder
        file = service.files().update(fileId=file_id, addParents=folder_id, fields='id, parents').execute()
        print("[+] Copying {} of {}".format(count, len(file_IDs)))
        count += 1


def main():
    arg_parser = usage()
    args = arg_parser.parse_args()
    if args.i is None or args.c is None:
        arg_parser.print_usage()
        sys.exit(-1)   
    config_file_handle = open(args.c, 'r')
    config = config_file_handle.readline().splitlines()[0]
    dest_folder = config.split(":")[1]
    copy_files(args.i, dest_folder)
    print("[+] Copying completed.")

if __name__ == '__main__':
    main()