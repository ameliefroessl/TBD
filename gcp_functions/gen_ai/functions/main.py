# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
import vertexai 
from vertexai.language_models import TextGenerationModel
from prompts import prompt_general_info, prompt_answer_question_from_file, prompt_physician_data, prompt_doublecheck_responses,prompt_comprehensible_summary

initialize_app()


### utils functions:

def prompt_palm(prompt_string,temperature=0.0,max_output_tokens=1024,model_name="text-bison@001"):
    """
    This function takes a prompt string, uses it to call the PALM api and returns the response string.
    args:
    prompt_string: String containing the final prompt for the model
    temperature: Temperature for the prediction call. Lower temperature means the most deterministic, least 'creative' output.
    max_output_tokes: 1024 is the maximum size for text-bison@001.
    """
    general_info_prompt_string = prompt_general_info(patient_record)

    # text-bison@001 is the generic PALMapi model for language tasks and questiona answering
    generation_model = TextGenerationModel.from_pretrained(model_name)

    response = generation_model.predict(general_info_prompt_string,temperature=temperature,max_output_tokens=max_output_tokens)
    return response


def check_content_extraction_coherence(patient_data,llm_response):
    """
    This function checks a PALM generated summary on coherency. It should return False if the PALM generated text contains extra information.
    REST api:
    "patient_data":raw text representation of a patient file
    "llm_response":a PALM-generated summary of the patient file
    """
        
    doublecheck_prompt_string = prompt_doublecheck_responses(patient_data,llm_response)
    
    response = prompt_palm(doublecheck_prompt_string)
    
    return (('yes' in response) and (not 'no' in response))


### https request bindings:
# They handle the decoding of https_fn into string arguments, call a python function to process, and returns the response re-packaged as https_fn

@https_fn.on_request()
def extract_diagnosis(req: https_fn.Request) -> https_fn.Response:
    """
    This function can be called to extract a short, comprehensive diagnosis from a given patient record in text representation.
    """
    if not "record" in req.args:
        return "No health record data provided."
    
    patient_record = req.args["record"]
    
    response = extract_diagnosis_(patient_record)
    return https_fn.Response(response.text)


@https_fn.on_request()
def answer_patient_question(req: https_fn.Request) -> https_fn.Response:
    """
    This function can be called to extract data from a patient file and answer a patient question concerning the patient file.
    REST api:
    "record":String representation of a patient file
    "question":User question concerning the patient file content
    """
        
    if not "record" in req.args:
        return "No health record data provided."
    if not "question" in req.args:
        return "No user question provided."
    
    patient_record = req.args["record"]
    patient_question = req.args["question"]
    
    response = answer_patient_question_response_(patient_record,patient_question)
    
    return https_fn.Response(response.text)

@https_fn.on_request()
def comprehensible_summary(req: https_fn.Request) -> https_fn.Response:
    """
    This function can be called to extract data from a patient file and create a comprehensible summary, where technical language is replaced by understandable terms, or technial terms are briefly explained.
    REST api:
    "record":String representation of a patient file
    """
        
    if not "record" in req.args:
        return "No health record data provided."
    
    patient_record = req.args["record"]
    
    response = comprehensible_summary_(patient_record)
    
    return https_fn.Response(response.text)

@https_fn.on_request()
def extract_contacts(req: https_fn.Request) -> https_fn.Response:
    """
    This function can be called to extract contact information from a patient file, e.g. in order to directly contact a physician on a mobile device.
    REST api:
    "record":String representation of a patient file
    """
        
    if not "record" in req.args:
        return "No health record data provided."
    
    patient_record = req.args["record"]
    
    response = comprehensible_summary_(patient_record)
    
    return https_fn.Response(response.text)


### proper python functions:

def extract_diagnosis_(patient_record):
    """
    This function can be called to extract a short, comprehensive diagnosis from a given patient record in text representation.
    """
    
    general_info_prompt_string = prompt_general_info(patient_record)

    response = prompt_palm(general_info_prompt_string)
    
    for i in range(10):
        if check_content_extraction_coherence(patient_record,response.text):
            continue
        else:
            general_info_prompt_string+=" Make sure not to add any added information that is not present in the patient report!\n"
            response = prompt_palm(general_info_prompt_string,temperature=0.1)
    
    return response

def answer_patient_question_(patient_record, patient_question):
    """
    This function can be called to extract data from a patient file and answer a patient question concerning the patient file.
    args:
    "record":String representation of a patient file
    "question":User question concerning the patient file content
    """
    
    user_question_prompt_string = prompt_answer_question_from_file(patient_record,patient_question)

    response = prompt_palm(user_question_prompt_string)

    return response

def comprehensible_summary_(patient_record):
    """
    This function can be called to extract data from a patient file and create a comprehensible summary, where technical language is replaced by understandable terms, or technial terms are briefly explained.
    args:
    "record":String representation of a patient file
    """
    
    comprehensive_prompt_string = prompt_comprehensible_summary(patient_record)

    response = prompt_palm(comprehensive_prompt_string)

    return response
    
def extract_contacts(patient_record):
    """
    This function can be called to extract contact information from a patient file, e.g. in order to directly contact a physician on a mobile device.
    args:
    "record":String representation of a patient file
    """
    
    response = prompt_physician_data(patient_record)
    
    return response