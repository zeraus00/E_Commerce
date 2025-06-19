from sqlalchemy import Column, String, Integer

from ecm.database.models import Base


class Users(Base):
    __tablename__= 'users'

    id : int = Column('id', Integer, primary_key=True, index=True, autoincrement=True)
    email : str = Column('email', String, nullable=False, index=True, unique=True)
    password : str = Column('password', String, nullable=False)

    def __init__(self, email, password, **kw):
        self.email = email
        self.password = password
        super().__init__(**kw)

