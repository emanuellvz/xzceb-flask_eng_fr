"""
Documento para traducir

"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):


    """
    Esta función recibe una palabra en inglés y la traduce a francés

    """
    translator = MyMemoryTranslator(source='english', target='french')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):


    """
    Esta función recibe una palabra en francés y la traduce a inglés

    """
    translator = MyMemoryTranslator(source='french', target='english')
    english_text = translator.translate(french_text)
    return english_text
