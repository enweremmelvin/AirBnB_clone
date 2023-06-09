#!/usr/bin/python3

from models.base_model import BaseModel


inst1 = BaseModel()
kwargs = inst1.to_dict()
inst2 = BaseModel(**kwargs)

print("Instance 1 ID: ", inst1.id)
print("Instance 2 ID: ", inst2.id)

print(inst1)
print("====================")
print(inst2)
