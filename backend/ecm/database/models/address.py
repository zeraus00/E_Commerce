from sqlalchemy import Column, Integer, String, ForeignKey

from backend.ecm.database.models import Base


class Address(Base):
    __tablename__ = 'address'

    id : int = Column('id', Integer, index=True, primary_key=True, autoincrement=True)
    user_id : int = Column('user_id', Integer,
                           ForeignKey('users.id', ondelete='cascade'), nullable=False)
    region : str = Column('region', String, nullable=False)
    province : str = Column('province', String, nullable=False)
    postal_code: str = Column('postal_code', String, nullable=False)
    municipality : str = Column('municipality', String, nullable=False)
    barangay: str = Column('barangay', String, nullable=False)

    def __init__(self,
                 user_id,
                 region,
                 province,
                 postal_code,
                 municipality,
                 barangay,
                 **kw):
        self.user_id = user_id
        self.region = region
        self.province = province
        self.postal_code = postal_code
        self.municipality = municipality
        self.barangay = barangay
        super().__init__(**kw)