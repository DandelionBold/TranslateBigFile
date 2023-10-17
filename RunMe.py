from LoadCSV import CSVFileWantToTranslate

import sys

def main():
    try:
        fromLanguage='en'
        targetLanguages = [
            'ar',
            # 'fr',
            # 'es',
            ]  # Add more languages as needed
        CSVFileWantToTranslate(
            inputCSVFile = 'Data.csv',
            outputCSVFile = 'TranslatedData.csv',
            sourceColumn = 'en',
            fromLanguage = fromLanguage,
            targetLanguages = targetLanguages,
            )
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    sys.exit(main())