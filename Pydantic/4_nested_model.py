from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
    

address_dict = {'city': 'Haridwar', 'state': 'Uttrakhand', 'pin': '122001'}

address1 = Address(**address_dict)

patient_name = {'name': 'irene', 'gender': 'female', 'age': 35, 'address': address1}

patient1 = Patient(**patient_name)

print(patient1.name)
print(patient1.age)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)