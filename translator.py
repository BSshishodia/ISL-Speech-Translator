from deep_translator import GoogleTranslator

def hindi_to_english(word):

    try:

        translated = GoogleTranslator(
            source='hi',
            target='en'
        ).translate(word)

        return translated.lower()

    except:

        return word.lower()