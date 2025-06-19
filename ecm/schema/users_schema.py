from pydantic import BaseModel, EmailStr


class UsersInput(BaseModel):
    email: EmailStr
    password: str


class UsersOut(BaseModel):
    id : int
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UsersInputPersonalInformation(BaseModel):
    user_id: int
    firstname: str
    middlename: str
    lastname: str
    suffix: str
    age: int
    sex: str
    contact_no : str


class UsersInputAddress(BaseModel):
    user_id: int
    region: str
    province: str
    postal_code: str
    municipality: str
    barangay: str