import requests, uuid
from GetEnvValue import getEnvValue 

class AzureTranslator:
    # Set my API properties form a env file

    # default constructor
    def __init__(self,fromLanguage='en', targetLanguages=['ar'], AZURE_TRANSLATOR_SERVICE_REST_API_KEY= 'AZURE_TRANSLATOR_SERVICE_REST_API_KEY', END_POINT='END_POINT', LOCATION_OR_REGION='LOCATION_OR_REGION', API_PATH='API_PATH'):
        # Define your Azure Translator resource endpoint and subscription key
        self.KEY = getEnvValue(AZURE_TRANSLATOR_SERVICE_REST_API_KEY)
        self.END_POINT = getEnvValue(END_POINT)

        # Set the location, also known as region (modify it according to your resource location)
        self.LOCATION_OR_REGION = getEnvValue(LOCATION_OR_REGION)

        # Set the API_PATH that you will use the API in this case its "/translate", (modify it according to your need)
        self.API_PATH = getEnvValue(API_PATH)

        # This just prepared the url for the request that will be send
        self.CONSTRUCTED_URL = self.END_POINT + self.API_PATH

        # Define the translation parameters
        self.params = {
            'api-version': '3.0',
            'from': fromLanguage,
            'to': targetLanguages,
        }

        self.headers = {
            'Ocp-Apim-Subscription-Key': self.KEY,
            'Ocp-Apim-Subscription-Region': self.LOCATION_OR_REGION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4()),
        }

    # Function to translate text using Azure Translation API
    def translateTextAzure(self, text):
        body = [{'text': text}]
        request = requests.post(self.CONSTRUCTED_URL, params=self.params, headers=self.headers, json=body)
        response = request.json()
        translations = response[0]['translations']
        translatedText = [t['text'] for t in translations]
        return translatedText