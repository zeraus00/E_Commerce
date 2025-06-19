from sqlalchemy import select

from ecm.database.engine import create_session
from ecm.database.models import PersonalInformation, Address
from ecm.database.models.users import Users

class UsersRepositories:

    @staticmethod
    async def create_user_account(users : Users,
                                  personal_info : PersonalInformation,
                                  address : Address):
       async with create_session() as db:
           try:
               db.add_all([users, personal_info, address])
               await db.commit()
           except Exception as e:
               await db.rollback()
               raise e

    @staticmethod
    async def get_user_by_email(email : str):
        async with create_session() as db:
            try:
                stmt = (select(Users)
                        .where(Users.email.ilike(email)))
                result = await db.execute(stmt)
                data = result.scalars().one_or_none()
                return data
            except Exception as e:
                raise e




