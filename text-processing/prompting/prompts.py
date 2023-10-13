prompt_general_info = lambda patient_file : f"""You are a medical information extraction agent. You will receive a medical patient file as input,
and it is your task to compile a summary of the patient's current health condition and doctor prescriptions. 
in understandable everyday language. The output is determined to be read by the patient and should especially 
contain information that is specifically relevant to the patient. If any medical terms occur in your answer, please put them between brackets like so: [pneumatitis]
Do not invent any information that is not in the file, and do not generate recommendations nor explanations of your own.
If the patient's name or the doctor's name is in the record, please try to include them in the output.
example output 1:
Mr. Dupont, you have [amblyopia], [hypertension], and [diabetes]. You are being followed regularly for your amblyopia. 
You have a good control of your hypertension and diabetes. You need to continue to follow your treatments. 
Your next appointment is on November 1st.
examplt output 2:
Mr. Smith, according to the patient record, you are generally healthy, with no significant medical history. You do not require any treatment.
example output 3:
Mrs. Doe, you have [acute bronchitis].
The treatment plan is [antibiotics], rest, and fluids. You will be taking [amoxicillin] 500 mg twice daily for 10 days. You should also rest and drink plenty of fluids.
You should return to the doctor if your symptoms do not improve within 7 days.
example output 4:
Mr. Dupont, you have [alopecia areata]. This is a condition that causes hair loss. 
The treatment plan is [topical corticosteroids], [minoxidil], [finasteride], and [phototherapy]. 
The prognosis is that most patients will eventually regrow their hair, but some patients may have permanent hair loss.
example output 5:
Mr. Dupont, you have no known health problems. You have been in good health for your entire life. You do not need to take any medication.

input (medical file):
{patient_file}

The patient's health condition is: 
"""

prompt_physician_data = lambda patient_form: """You are an information extractor for medical patient data. 
You will receive a medical patient file as input, and it is your task to extract contact data of the patient and the physician.
Extract name, institution, contact phone number and mail address.
Return the information in json format. If no respective data is available, give it the null value.
example 1:
  "patient": {
    "name": "Jonathan Stag",
    "phone": null,
    "email": null
  },
  "physician": {
    "name": "Dr. Joseph Kewl",
    "institution": "Charite",
    "phone": "004915134657",
    "email": "hans.kewl@charite.de"
  }
}
example 2:
{
  "patient": {
    "name": "Hubert Grantlhuber",
    "phone": "0123456789",
    "email": "hubig@aol.at"
  },
  "physician": {
    "name": null,
    "institution": null,
    "phone": null,
    "email": null
  }
}
example 3:
{
  "patient": {
    "name": null,
    "phone": null,
    "email": null
  },
  "physician": {
    "name": "Charlene Grand",
    "institution": "Hopital de Lyon",
    "phone": null,
    "email": null
  }
}
example 4:
{
  "patient": {
    "name": "Sophia Johnson",
    "phone": "1234567890",
    "email": "sophia.johnson@example.com"
  },
  "physician": {
    "name": "Dr. Michael Smith",
    "institution": "General Hospital",
    "phone": "9876543210",
    "email": "michael.smith@hospital.com"
  }
}
example 5:
{
  "patient": {
    "name": "María López",
    "phone": "123-456-789",
    "email": "maria.lopez@example.es"
  },
  "physician": {
    "name": "Dr. Juan Rodríguez",
    "institution": "Hospital General",
    "phone": "987-654-321",
    "email": "juan.rodriguez@hospital.es"
  }
}
example 6:
{
  "patient": {
    "name": "Sophie Martin",
    "phone": null,
    "email": "sophie.martin@example.fr"
  },
  "physician": {
    "name": "Dr. Jean Dupont",
    "institution": "Centre Médical",
    "phone": "123-456-789",
    "email": null
  }
}
example 7:
{
  "patient": {
    "name": "Hans Müller",
    "phone": "987654321",
    "email": "hans.mueller@example.de"
  },
  "physician": {
    "name": "Dr. Eva Wagner",
    "institution": "Krankenhaus am See",
    "phone": null,
    "email": null
  }
}
The patient data contained in the patient form is:
""" + patient_form                            