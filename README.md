# TranslateBigFile

<p align="center">
    <img width="180" src="https://icons.iconarchive.com/icons/marcus-roberto/google-play/512/Google-Translate-icon.png" alt="logo.">
</p>
<p align="center">

This repo just for translation csv table to any language using Azure Translator Service REST API, 2023.

# Main functionality

This project main functionality is to connect to Azure Translator Service REST API and ask to translate given text.

TranslateBigFile aims to be:

- **Easy to use**
- **Flexible** to support many languages
- **Powerful** by using ai chatGPT

> This project was built using [GitHub Pages](https://pages.github.com/) and [Python 3.10.0](https://www.python.org/downloads/release/python-3100/).

## Building and developing

If you want to setup TranslateBigFile from source you will need

You only need to run install the Python, once it installeed in the repository environment just run the following command to install needed libraries `pip install -r requirements.txt` after installing python. This will install all you want. You should **not** run `pip install -r requirements.txt` in each time.

Each file has its own build instructions in its own function.

## How to use it?
- You need to make file named `.env` this file will have in it some properties as following
 ``` .env
 AZURE_TRANSLATOR_SERVICE_REST_API_KEY=78973127983342197419801923879138
 END_POINT=https://api.yourApi.Name.com
 LOCATION_OR_REGION=YourLocation
 API_PATH=/translate
 ```
 To get your Azure Translator Service endpoint, follow these steps:
    1. Go to the Azure portal.
    1. Sign in to your Azure account.
    1. Click on the Menu icon (three horizontal lines) in the top left corner of the page.
    1. Click on All resources.
    1. search your Azure Translator Service resource and click on it.
    1. In the Overview tab, you will choose the plan and click create. (or just go to [this link](https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Marketplace/GalleryItemDetailsBladeNopdl/id/Microsoft.CognitiveServicesTextTranslation/selectionMode~/false/resourceGroupId//resourceGroupLocation//dontDiscardJourney~/false/selectedMenuId/home/launchingContext~/%7B%22galleryItemId%22%3A%22Microsoft.CognitiveServicesTextTranslation))
 After that you will find the data you want