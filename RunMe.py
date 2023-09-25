from LoadCSV import CSVFileWantToTranslate

import sys

def main():
    try:
        CSVFileWantToTranslate(inputCSVFile = 'Data.csv', outputCSVFile = 'TranslatedData.csv', columnNameThatWillTranslate = 'Main', targetLanguage = 'Arabic')
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    sys.exit(main())