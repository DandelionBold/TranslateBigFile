import openai
from GetEnvValue import getEnvValue 

# Set my API key form a env file
apiKey = getEnvValue('OPEN_AI_KEY')

# Initialize my OpenAI API client
openai.api_key = apiKey

# Define a function to translate text
def translateText(textToTranslate, targetLanguage, model = 'gpt-3.5-turbo'):
    response = openai.Completion.create(
        engine = model, # Use the appropriate GPT-3 engine
        prompt = f"Translate the following text to {targetLanguage}: {textToTranslate}",
        max_tokens = 5,
        n = 1  # Number of responses
    )
    translatedText = response.choices[0].text.strip()
    return translatedText
