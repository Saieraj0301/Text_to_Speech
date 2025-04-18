from TTS import text_to_speech
from Summarizer import summarize_text
from googletrans import Translator

translator = Translator()

def pipeline(text, lang='en', use_summary=True, strength=50, translate_before_tts=True):
    original_wc = len(text.split())
    summarized_text = text

    if use_summary:
        summarized_text = summarize_text(text, strength=strength)

    summarized_wc = len(summarized_text.split())

    if translate_before_tts and lang != 'en':
        translated = translator.translate(summarized_text, dest=lang)
        summarized_text = translated.text

    audio_file = text_to_speech(summarized_text, lang=lang)

    return audio_file, summarized_text, original_wc, summarized_wc
