import pandas as pd
from ChatGPT import translateText


def CSVFileWantToTranslate(inputCSVFile, outputCSVFile, columnNameThatWillTranslate, targetLanguage):
    df = pd.read_csv(inputCSVFile)
    translatedColumn = targetLanguage.lower()[:2]


    for index, row in df.iterrows():
        sourceText = row[columnNameThatWillTranslate]
        print(index)
        print(sourceText)
        # Use OpenAI's ChatGPT for translation
        translatedText = translateText(sourceText, targetLanguage)
        row[translatedColumn] = translatedText
        print(row[translatedColumn])

    df.to_csv(outputCSVFile, index=False)
