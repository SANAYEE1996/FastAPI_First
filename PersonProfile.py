from pydantic import BaseModel

class PersonProfile(BaseModel):
    name : str
    age : int