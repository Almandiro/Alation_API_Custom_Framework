#*******************************************************************************
# Author of Original Script: Ellen Hudson-Snyder
# Updated / Adapted by: Ali Daneshmand
#                       (ali.daneshmand@inceptds.com)
#                       (ali.daneshmand@saic.com)
# 
#
# This is a sample Python script that can be used to import Business Glossary
# Terms into your Alation instance.
#*******************************************************************************

#*******************************************************************************
# IMPORT LIBRARIES
#*******************************************************************************
import json
import csv
import requests
import pandas as pd
import numpy as np
from tqdm import tqdm
import logging
import urllib3
import sys


def bulkGlossaryIngestion(fileName, sheetName):
    #Disables HTTPS Warnig assuming that the HTTPS error message is only a warning.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #*******************************************************************************
    # ALATION API Connection Updates
    #*******************************************************************************

    #Grabbing Token and Base URL from another file.
    #This is simply to keep some level of PII protection.
    from alation_api import alation_dev_token
    from alation_api import alation_dev_base_url

    alation_api_end_point = '/api/v1/bulk_metadata/custom_fields/'
    objecttype = '/article'
    content = 'application/json'
    headers = {'token': alation_dev_token, 'Content-Type': content}

    logging.basicConfig(level=logging.INFO,
                    filename="alation_uploader.log", filemode="w+",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt='%Y-%m-%d %H:%M:%S', )

    #*******************************************************************************
    # Hard Coding Excel File To Upload
    #*******************************************************************************

    excelfilename = str(fileName)
    excel_file = pd.ExcelFile(excelfilename)
    sheets = excel_file.sheet_names

    logging.info(f"Excel File Name: {excelfilename} \nExcel Sheets: {sheets}")

    #*******************************************************************************
    # Excel File Manipulation & Ingestion to Alation Data Catalog via API
    #
    # This section makes use of a nested For Loop to traverse through each Excel
    # Sheet, and each row per sheet
    #*******************************************************************************

    for sheet in sheets:
        logging.info(f"Traversing For-Loop \n\nCurrent Sheet {sheet}")
        #Designating specific Sheet in the Excel Spreadsheet to ingest
        if sheet == str(sheetName):

            article_template = 'Test_Upload_Template'  # Name of the custom template in Alation
            api_url = alation_dev_base_url + alation_api_end_point + article_template + \
                      objecttype + '?create_new=true&replace_values=true'
            df = excel_file.parse(sheet)
            logging.info(df)

            #*******************************************************************************
            # This is an addition to the original example provided by Ellen.  Given that the
            # XLSX file contains many empty cells, Alation would throw errors.  This command
            # was added to fill in the empty fields with something so that the NULL fields
            # don't cause issues.
            #*******************************************************************************

            df = df.fillna("BLANK")

            counter=1

            # Traversing through each row of the specific article
            for index, row in tqdm(df.iterrows()):
                counter=counter+1

                if counter <= 0:
                    print("Skipping")
                else:
                    try:
                        title = str(row[0])
                        abbreviation = str(row[1])
                        definition = str(row[2])

                        key = title

                        # Template 1: Key Report Inventory
                        # Template 2: Data Governance Standards and Terms
                        # Template 3: Learning and Reference
                        # Template 4: myData Business Operations Terms

                        #kri_api_data = {"key": key, "title": title, "abbreviation": abbreviation, "definition": definition, "data classification": "Data%20Classification", "related data": Related%20Data, "status": Status}
                        #dgst_api_data = {"key": key, "title": title, "abbreviation": abbreviation, "definition": definition}
                        #lar_api_data = {"key": key, "title": title, "abbreviation": abbreviation, "definition": definition}
                        #busterms_api_data = {"key": key, "title": title, "abbreviation": abbreviation, "definition": definition}
                        

                        api_data = {"key": key, "title": title, "abbreviation": abbreviation, "definition": definition}

                        res = requests.post(api_url, json=api_data, headers=headers, verify=False)
                        #print("HTTP Response: " + str(res.status_code) + " Status: " + res.text)

                        if res.status_code == 401:
                            print ("Check Your Access Token to see if it's Expired, Revoked, or Deleted.")
                            print ("If you do not have an Alation Token, contact your Alation System Administrator.")
                            exit()
                        if res.status_code not in [200, 202]:
                            print(row, res)

                    except Exception as e:
                        print(e, file=sys.stderr)
                        logging.info(e)
                        exit()
