from logging import raiseExceptions

from fastapi import HTTPException, status

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse

from ecm.database.repositories.users_repositories import UserRepositories
from ecm.schema.users_schema import UsersInput, UsersInputPersonalInformation, UserInputAddress, UsersOutput
from ecm.services.users_services import UserServices
from ecm.utils.auth_utils import AuthUtils

auth_router = APIRouter(
tags=['verification / Authentication']
)

@auth_router.post('/create-account')
async def create_account(users_cred : UsersInput,
            users_p_info : UsersInputPersonalInformation,
            users_address : UserInputAddress):
    try:
        return await UserServices.create_user_account(
            users_cred, users_p_info, users_address
        )
    except Exception as e:
        raise e

@auth_router.post('/authenticate-user')
async def authenticate_user_credential(form_data : OAuth2PasswordRequestForm = Depends()):
    try:
        data = await UserRepositories.get_user_by_email(form_data.username)

        if not data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Email not found!'
            )

        data = jsonable_encoder(UsersOutput.model_validate(data).model_dump())
        is_password_correct = AuthUtils.authenticate_user(data, form_data.password)

        if not is_password_correct:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Incorrect Password!'
            )

        to_encode = data.copy()
        del data['password']

        access_token = AuthUtils.generate_access_token(to_encode)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                'status' : 'OK',
                'message' : access_token,
                'acess_token' : 'bearer'
            }
        )
    except Exception as e:
        raise e

