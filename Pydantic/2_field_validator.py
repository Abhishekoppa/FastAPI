from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator('email')
    @classmethod
    def email_validation(cls, value):
        valid_domain = ['hdfc.com', 'icici.com', 'gmail.com']
        
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domain:
            raise ValueError("Tera domain galat h be")
        
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')


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
    'age': 55,
    'weight': 55.55,
    'married': False,
    'allergies': ['onlyIrene', 'onlySana', 'Asuna', 'Nancy', 'Aayushma'],
    'contact_details': {
        'phone': '9238479037'
    }
}


myPat = Patient(**patient_info)

update_patient_data(myPat)