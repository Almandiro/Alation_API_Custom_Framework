import requests
import json
import urllib3
import ssl


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# This is an example token. Please replace this with your token.
headers = {'Token': '9ywKLNKjCLeVr8M2msKYwI5Fpx7xLQQqtohwQDVV0aM'}


# Request all articles with a specific template, Add the template ID to the URL
response = requests.get('https://catalog.mydatadev.saic.com/integration/v1/article/', headers=headers, verify=False)

articles = json.loads(response.text)
counter = 0
for article in articles:
    if len(article["custom_templates"]) > 0: 
        # Use term IDs to delete the article
        #response2 = requests.delete('https://catalog.mydatadev.saic.com/integration/v1/article/' + str(article['id']), headers=headers, verify=False)
        counter = counter + 1
        
print("Done. " + str(counter) + " articles removed")