import requests
import urllib3
import sys

#Disables HTTPS Warnig assuming that the HTTPS error message is only a warning.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#*******************************************************************************
# ALATION API Default Connection Information
#*******************************************************************************

#Grabbing Token and Base URL from another file.
#This is simply to keep some level of PII protection.
from alation_api import alation_dev_token
from alation_api import alation_dev_base_url

#*******************************************************************************
# ALATION API Connection to specific Alation API Functionality (If Needed)
#*******************************************************************************


#For "Bulk Ingestion", simply import the function from the "Library File" and
#run the Ingestion function, with the appropriate arguements that need to be
#passed

