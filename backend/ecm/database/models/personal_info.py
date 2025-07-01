from sqlalchemy import Column, String, Integer, ForeignKey

from backend.ecm.database.models import Base
class PersonalInformation(Base):
    __tablename__ = 'personal_info'

    id: int = Column('id', Integer, primary_key=True, autoincrement=True)
    user_id : int = Column('user_id', Integer,
                           ForeignKey('users.id', ondelete='cascade'), nullable=False)
    firstname: str = Column('firstname', String, nullable=False)
    middlename: str = Column('middlename', String, nullable=True)
    lastname: str = Column('lastname', String, nullable=False)
    suffix: str = Column('suffix', String, nullable=True)
    age: int = Column('age', Integer, nullable=False)
    sex: str = Column('sex', String, nullable=False)
    contact_no : str = Column('contact_no', String, nullable=False)
    def __init__(self,
                 user_id,
                 firstname,
                 middlename,
                 lastname,
                 suffix,
                 age,
                 sex,
                 contact_no,
                 **kw):
        self.user_id = user_id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.suffix = suffix
        self.age = age
        self.sex = sex
        self.contact_no = contact_no
        super().__init__(**kw)