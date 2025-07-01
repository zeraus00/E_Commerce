from fastapi import HTTPException

from starlette.responses import JSONResponse
from fastapi import status
from backend.ecm.database.repositories.users_repositories import UserRepositories
from backend.ecm.schema.users_schema import UsersInput, UsersInputPersonalInformation, UserInputAddress
from backend.ecm.utils.auth_utils import AuthUtils


class UserServices:

    @staticmethod
    async def create_user_account(
            users_cred : UsersInput,
            users_p_info : UsersInputPersonalInformation,
            users_address : UserInputAddress
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
                suffix=users_p_info.suffix,
                age=users_p_info.age,
                sex=users_p_info.sex,
                contact_no=users_p_info.contact_no
            )

            users_address_m = Address(
                user_id=users_address.user_id,
                region=users_address.region,
                province=users_address.province,
                postal_code=users_address.postal_code,
                municipality=users_address.municipality,
                barangay=users_address.barangay
            )

            if await UserRepositories.get_user_by_email(users_cred_m.email):
                raise HTTPException(
                    status_code = status.HTTP_400_BAD_REQUEST,
                    detail = "Email is already exist"
                )

            await UserRepositories.create_user_account(
                users=users_cred_m,
                personal_info=users_p_info_m,
                address=users_address_m
            )

            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={'status' : 'ok',
                         'message' : 'successfully created'}
            )
        except Exception as e:
            raise e
