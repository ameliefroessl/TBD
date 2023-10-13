# This is TBD's prompt processing script
# It contains a number of functions that process medical patient data text representations

from firebase_functions import https_fn
from firebase_admin import initialize_app
import vertexai 
from vertexai.language_models import TextGenerationModel

initialize_app()


@https_fn.on_request()
def prompt_palm_ai(req: https_fn.Request) -> https_fn.Response:
    """
    This function send a generic prompt to the PALMapi. 
    The prompt text is defined in the REST arg "prompt"
    """

    # text-bison@001 is the generic PALMapi model for language tasks and questiona answering
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")

    response = generation_model.predict(prompt=req.args["prompt"])

    return https_fn.Response(response.text)


@https_fn.on_request()
def extract_diagnosis(req: https_fn.Request) -> https_fn.Response:
    """
    This function can be called to extract a short, comprehensive diagnosis from a given patient record in text representation.
    """
    
    from prompts import prompt_general_info
    
    if not "record" in req.args:
        return "No health record data provided."
    
    patient_record = prompt=req.args["record"]
    
    general_info_prompt_string = prompt_general_info(patient_record)

    # text-bison@001 is the generic PALMapi model for language tasks and questiona answering
    generation_model = TextGenerationModel.from_pretrained("text-bison@001")

    response = generation_model.predict(general_info_prompt_string,temperature=0.0,,max_output_tokens = 1024)

    return https_fn.Response(response.text)


