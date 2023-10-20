# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from google.cloud import vision
from google.cloud import storage

initialize_app()


def download_file_from_bucket(remote_url, local_url):
    storage_client = storage.Client()
    bucket_name = "merantix-genai23ber-9514.appspot.com"
    bucket = storage_client.get_bucket(bucket_name)
    bucket.download_to_filename(local_url)


def format_output(texts):
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


def detect_text_local(path):
    client_options = {"api_endpoint": "eu-vision.googleapis.com"}
    client = vision.ImageAnnotatorClient(client_options=client_options)

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotation
    return format_output(texts)


def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web."""
    client_options = {"api_endpoint": "eu-vision.googleapis.com"}

    client = vision.ImageAnnotatorClient(client_options=client_options)
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return format_output(texts)


# WIP -- this should work something along these lines
# @https_fn.on_request()
# def ocr_download(req: https_fn.Request) -> https_fn.Response:

#     remote_url = detect_text_uri(uri=req.args["image_url"])
#     local_url = "/tmp/test.jpg"
#     # Read image data directly from request body
#     download_file_from_bucket(remote_url, local_url)
#     # image_data = req.data
#     # Use the bytes data function to detect text
#     text_in_image = detect_text_local(path=local_url)
#     return https_fn.Response(text_in_image)


@https_fn.on_request()
def ocr_v2(req: https_fn.Request) -> https_fn.Response:

    text_in_image = detect_text_uri(uri=req.args["image_url"])

    return https_fn.Response(text_in_image)
