
# Description
A Python Script to copy shared google drive folders/files to another Drive Folder.
It uses the Google Drive API v3. It is built using Python3, though it could work with Python 2.7.x
with minimal modification.

# To Run

## 1) Install the requirements as follows

`pip3 install -r requirements.txt`

## 2) Enable Google Drive API and install libraries
You need to enable Google Drive API to use this script. To do this, go to
 [Drive API Quickstart](https://developers.google.com/drive/api/v3/quickstart/python) 
and follow steps 1 and 2 as shown on that page. It is quite an easy process. 
Make sure you download and save the **credentials.json** file to the directory where this script is. 

## 3) Provide list of the IDs of the shared folders/files to copy.
All folders and files on Google Drive have a unique ID that identifies them. For example, a shared folder might look as follows:

`https://drive.google.com/drive/folders/17QSblfUNNYlookingSTRINGshare?usp=sharing`

The ID for this shared folder is that funny looking string : 17QSblfUNNYlookingSTRINGshare 
You must provide a list of all the IDS of the folders/files in a text file, one per line. See **SAMPLE_IDs.txt** for the format the script expects.

## 4) Provide the ID of the folder you would like to copy the shared folders/files to.
---
Finally, you need to provide the ID of the folder where you would like to. To get this ID, open the folder you want to copy the files to in your browser. The URL in your address bar should look something like the one below:

`https://drive.google.com/drive/u/0/folders/19x2AintThisFunSonUKnowsPSYay`

The ID for this folder is 19x2AintThisFunSonUKnowsPSYay. Copy that ID and paste it in the **CONFIG.txt** in the directory. The script will read the destination folder from this file.

## 5) Run the script.
`python3 copy_shared_folders -i SHARED_FOLDER_IDs.txt -c CONFIG.txt`

Where ***SHARED_FOLDER_IDs.txt*** is a file containing the IDs of the shared folders/files and 
***CONFIG.txt*** is the configuration file containing the ID of the destination folder.

When you run it for the first time, it will open your web browser and ask you to login with your Google account and authorize the script to manage your drive account - aunthenticate as necessary.