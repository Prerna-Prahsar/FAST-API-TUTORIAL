from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name : Annotated[str, Field(default='Khushi', max_length= 50, title='Name of the Patient', description='Give the name of the patient in less than 50 char', examples = ['Prerna', 'Khushi'])]                         #str = Field(max_length=50)# deafault value
    email: EmailStr
    linkedn_profile : AnyUrl 
    age  : int
    weight : Annotated[float , Field(gt =0 , lt= 120, strict=True)]
    married : Annotated[bool, Field(default=None, description='Is the patient married or not')]           #Optional[bool] = None # optional  
    allergies : Optional[List[str]]  = Field(max_length=5) # for two level verification
    contact_details : Dict[str, str]

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print('inserted into database')
    
    
def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print('update')

    
Patient_info = {'name' :'Sumit', 'age' : 30,'email': 'kj2006@gmail.com', 'linkedn_profile': 'http://linkedin.com/1234', 'weight': 98,'allergies':
    ['pollen', 'dust'], 'contact_details' : {'email': 'abc@gmail.com', 'phone':'2353462'}}
    
patient1 = Patient(**Patient_info)

insert_patient_data(patient1)

# Patient_info = {'name': 'Prerna', 'age' : 22, 'weight': 70}

patient2 = Patient(**Patient_info)
update_patient_data(patient2)


