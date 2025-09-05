from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print('BMI',patient.bmi)
    print(patient.married)
    print('-'*50)
    

patient_info = {
    'name': "Irene Sana Poudel", 'email': 'maichahutujimeriirenesana@gmail.com', 'linkedin_url': 'http://linkedin.com/1322', 'age': 77,
    'weight': 55.55, 'height': 1.72, 'married': False, 'allergies': ['onlyIrene', 'onlySana', 'Asuna', 'Nancy', 'Aayushma'],
    'contact_details': {
        'phone': '9238479037',
        'emergency': '2343'
    }
}
myPat = Patient(**patient_info)
update_patient_data(myPat)