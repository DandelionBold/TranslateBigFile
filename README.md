# TranslateBigFile

<p align="center">
    <img width="180" src="https://icons.iconarchive.com/icons/marcus-roberto/google-play/512/Google-Translate-icon.png" alt="logo.">
</p>
<p align="center">

This repo just for translation csv table to any language using chat gpt 3.5 engine, 2023.

# Main functionality

This project main functionality is to connect to chatGPT and ask to translate given text.

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
- You need to make file named `.env` this file will have key like this `OPEN_AI_KEY=sk-dhwjkb2ehdbewkjbqjh3berdekjbwqekf239qfef2hfjb23e`, this key can you get from [ChatGPt Website](https://platform.openai.com/account/api-keys)
- In File [ChatGPT.py](https://github.com/DandelionBold/TranslateBigFile/blob/main/ChatGPT.py) you change the engine and token number based on your needs, look for types of [engines](https://gptforwork.com/guides/openai-gpt3-models) for chatGPT
