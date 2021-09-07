import pandas as pd 
import os 
import pymsteams

# change directory to downloads 
os.chdir('/usr/src/app/downloads')

# open CSV and import 2 columns (Unique ID and Parent Access Code) 
parentAccessCodes = pd.read_csv("parent-code-export.csv", keep_default_na=False, usecols=['Unique ID', 'Parent Access Code'])

# remove 'STU_' from the Unique ID column
parentAccessCodes['Unique ID'] = parentAccessCodes['Unique ID'].str.replace(r'STU_', '')

# add columns to parentAccessCodes dataframe
parentAccessCodes['CO'], parentAccessCodes['ELK'], parentAccessCodes['ELK2'], parentAccessCodes['CO2'], parentAccessCodes['SLK'] = 'ENG', 'ESLI', 'EVID', 'SPA', 'SSLI'

# create CSV from parentAccessCodes dataframe
parentAccessCodes.to_csv("PAC.csv", index=False)

# send Teams webhook when process is complete
myTeamsMessage = pymsteams.connectorcard("https://tustin.webhook.office.com/webhookb2/9b433de8-0c41-468d-b3ba-fac9a49ccd4f@82a845ce-0042-4a08-a2f1-734fbdc34806/IncomingWebhook/772c4e953aa14c8383ca99b4f7d6fc50/6c792152-820a-4183-a14f-1273fa3e3a4e")
myTeamsMessage.title("Automated process complete (Schoology PAC.CSV exported)")
myTeamsMessage.text("Schoology Parent Access Codes CSV file saved to server")

# # print message preview 
# myTeamsMessage.printme()
# send the message
myTeamsMessage.send()