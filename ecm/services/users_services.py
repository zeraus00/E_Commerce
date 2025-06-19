from starlette.responses import JSONResponse
from fastapi import status, HTTPException

from ecm.database.models import *
from ecm.database.repositories.users_repositories import UsersRepositories
from ecm.schema.users_schema import UsersInput, UsersInputPersonalInformation, UsersInputAddress
from ecm.utils.auth_utils import AuthUtils


class UsersServices:

    @staticmethod
    async def create_user_account(
            users_cred: UsersInput,
            users_p_info: UsersInputPersonalInformation,
            users_address: UsersInputAddress
    ):
        try:
            hashed_pass = AuthUtils.hash_password(users_cred.password)
            users_cred_m = Users(
                email=users_cred.email,
                password=hashed_pass
            )

            users_p_info_m = PersonalInformation(
                user_id=users_p_info.user_id,
                firstname=users_p_info.firstname,
                middlename=users_p_info.middlename,
                lastname=users_p_info.lastname,
                age=users_p_info.age,
                sex=users_p_info.sex,
                suffix=users_p_info.suffix,
                contact_no=users_p_info.contact_no
            )
            users_address_m = Address(
                user_id=users_address.user_id,
                barangay=users_address.barangay,
                province=users_address.province,
                postal_code=users_address.postal_code,
                municipality=users_address.municipality,
                region=users_address.region
            )

            #Check the email, if exist in db
            if await UsersRepositories.get_user_by_email(users_cred_m.email):
                raise HTTPException(
                    status_code = status.HTTP_400_BAD_REQUEST,
                    detail = "Email is already exist!"
                )

            await UsersRepositories.create_user_account(
                users=users_cred_m,
                personal_info=users_p_info_m,
                address=users_address_m
            )

            return  JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={"status": 'ok',
                         'message': 'successfully created!'}
            )
        except Exception as e:
            raise e

