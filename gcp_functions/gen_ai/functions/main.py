# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
import vertexai 
from vertexai.language_models import TextGenerationModel

initialize_app()


@https_fn.on_request()
def prompt_palm_ai(req: https_fn.Request) -> https_fn.Response:

    # text-bison@001 is the generic PALMapi model for language tasks and questiona answering
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")
    response = generation_model.predict(prompt=req.args["prompt"])

    return https_fn.Response(response.text)
   