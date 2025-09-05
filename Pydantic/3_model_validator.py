from pydantic import BaseModel, EmailStr, model_validator, Field
from typing import List, Dict, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Annotated[Dict[str, int], Field(default=None)] 
    
    
    @model_validator(mode ="after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Kindly please add Emergency number for your own safety.")
        
        return model
    

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('-'*50)
    

patient_info = {
    'name': "Irene Sana Poudel",
    'email': 'maichahutujimeriirenesana@gmail.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': 77,
    'weight': 55.55,
    'married': False,
    'allergies': ['onlyIrene', 'onlySana', 'Asuna', 'Nancy', 'Aayushma'],
    'contact_details': {
        'phone': 9238479037,
        'emergency': '2343'
    }
}


myPat = Patient(**patient_info)

update_patient_data(myPat)
    
    