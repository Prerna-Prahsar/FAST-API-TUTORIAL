from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated
 
class Patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight : float # kg
    height : float  # meter
    married : bool 
    allergies : List[str]
    contact_details : Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) ->float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    
    
def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': 64, 'weight': 80,'height' : 1.68, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', 'emergency': '9931227170'}}

patient1 = Patient(**patient_info) # validation -> type coercion

update_patient_data(patient1)
    