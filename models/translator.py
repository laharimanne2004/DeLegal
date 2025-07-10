from langdetect import detect
from transformers import MarianMTModel, MarianTokenizer, pipeline

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def translate_to_english(text):
    lang = detect_language(text)
    if lang == "en":
        return text

    lang_map = {
        "hi": "Helsinki-NLP/opus-mt-hi-en",
        "te": "Helsinki-NLP/opus-mt-mul-en"  # <-- Updated here
    }

    if lang in lang_map:
        model_name = lang_map[lang]
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        translator = pipeline("translation", model=model, tokenizer=tokenizer)
        translation = translator(text, max_length=512)[0]['translation_text']
        return translation

    return text
