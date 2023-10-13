# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from google.cloud import vision

initialize_app()

def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web."""
    client_options = {"api_endpoint": "eu-vision.googleapis.com"}

    client = vision.ImageAnnotatorClient(client_options=client_options)
    # client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    all_text = []
    for text in texts:  
        all_text.append(text.description)
    all_text = " ".join(all_text)
    return all_text

    if response.error.message:
        return (
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )


@https_fn.on_request()
def ocr_v2(req: https_fn.Request) -> https_fn.Response:

    text_in_image = detect_text_uri(uri=req.args["image_url"])

    return https_fn.Response(text_in_image) 