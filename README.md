# Power BI integration With google spreadsheet using pyhton

To connect Python's to Google products you're gonna need to set OAUTH Client ID's 
Please go to this webpage and follow the instructions to setup https://developers.google.com/sheets/api/quickstart/python

use the following command to install the packages that we're gonna use

download the OAUTH token and rename to "Credentials.json"

## Configuring Python

Use the following command to install the packages that we're gonna use over procces

```
pip install -r requirements.txt

```

before we need to setup the script parameter's, go to RunLocal.py and change the values inside <>
the spreeadsheet ID you're gonna find in the url from the spreeadshet, something like this
https://docs.google.com/spreadsheets/d/ <spreadsheetId> /edit#gid=15....


## Importing direct in PBI

in Power Bi

1- go in Get Dataset
2- click in more
3- in search bar type script
4- click in pyhon script
5- copy the following command below and paste in the text area

```
import sys

myPath = '<c:/users/username/folder>'
SPREADSHEET_ID='<SPREADSHEET_ID>'
Range='<Range>'

sys.path.append(myPath)

from gplanilhas import gPlanilhas
import os

os.chdir(myPath)

df = gPlanilhas().main(SPREADSHEET_ID,Range)

```

6- change the value <ScriptPath> to where your python script is localized ** all your myPath must be with / instead of \ **
example: myPath = 'c:/users/username/folder'
