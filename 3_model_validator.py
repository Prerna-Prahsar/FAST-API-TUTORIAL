from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

# if age is greater than 60 , then there must be a emergency phone no: 
class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight : float
    married : bool 
    allergies : List[str]
    contact_details : Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model
    
    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': 64, 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency': '9931227170'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)
    