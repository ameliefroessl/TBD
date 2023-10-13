# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
import vertexai 
from vertexai.language_models import TextGenerationModel
from prompts import prompt_general_info

initialize_app()


# @https_fn.on_request()
# def prompt_palm_ai(req: https_fn.Request) -> https_fn.Response:

#     # text-bison@001 is the generic PALMapi model for language tasks and questiona answering
#     generation_model = TextGenerationModel.from_pretrained("text-bison@001")
#     response = generation_model.predict(prompt=req.args["prompt"])

#     return https_fn.Response(response.text)

def prompt_palm(patient_record):
    general_info_prompt_string = prompt_general_info(patient_record)

    # text-bison@001 is the generic PALMapi model for language tasks and questiona answering
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")

    response = generation_model.predict(general_info_prompt_string,temperature=0.0,max_output_tokens = 1024)
    return response


@https_fn.on_request()
def extract_diagnosis(req: https_fn.Request) -> https_fn.Response:
    """
    This function can be called to extract a short, comprehensive diagnosis from a given patient record in text representation.
    """
    
    if not "record" in req.args:
        return "No health record data provided."
        
    response = prompt_palm(patient_record=req.args["record"])
    
    return https_fn.Response(response.text)
