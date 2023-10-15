# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from google.cloud import translate_v2 as translate

initialize_app()

@https_fn.on_request()
def translate(req: https_fn.Request) -> https_fn.Response:
    translate_client = translate.Client()

    # the text you want translated, the model does automatic source language detection 
    text = req["text"]
    # target language in ISO 639-1 language code
    target_lan = req["language"]

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target_lan)
    return https_fn.Response(result["translatedText"])
