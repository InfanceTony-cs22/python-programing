#google translator
from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    input_text = input("Enter the text to translate: ")
    target_language = input("Enter the target language (e.g., 'en' for English): ")

    translated_text = translate_text(input_text, target_language)
    
    print(f"Translated Text: {translated_text}")
