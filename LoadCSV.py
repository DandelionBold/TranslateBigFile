import pandas as pd
from AzureTranslatorServiceRESTAPI import AzureTranslator



def CSVFileWantToTranslate(inputCSVFile, outputCSVFile, sourceColumn, fromLanguage, targetLanguages):
    AZURE_TRANSLATOR_SERVICE_REST_API_KEY= 'AZURE_TRANSLATOR_SERVICE_REST_API_KEY'
    END_POINT='END_POINT'
    LOCATION_OR_REGION='LOCATION_OR_REGION'
    API_PATH='API_PATH'

    azureTranslator = AzureTranslator(fromLanguage=fromLanguage, targetLanguages=targetLanguages, AZURE_TRANSLATOR_SERVICE_REST_API_KEY= AZURE_TRANSLATOR_SERVICE_REST_API_KEY, END_POINT=END_POINT, LOCATION_OR_REGION=LOCATION_OR_REGION, API_PATH=API_PATH)
    # print(azureTranslator.translateTextAzure("You are about to delete the selected item(s). Do you want to proceed?"))
    
    
    df = pd.read_csv(inputCSVFile)

    for index, row in df.iterrows():
        sourceText = row[sourceColumn]
        translatedTexts = azureTranslator.translateTextAzure(sourceText)
        for i, translatedText in enumerate(translatedTexts):
            df.at[index, targetLanguages[i]] = translatedText
            df.at[index, 'IsTranslated'] = 'TRUE'
            print()
            print(str(index) + ")")
            print("translatedText:" + sourceText)
            print("translatedText:" + translatedText)
            print()
        # break
    df.to_csv(outputCSVFile, index=False, encoding="utf-8-sig")
