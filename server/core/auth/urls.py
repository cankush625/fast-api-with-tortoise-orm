from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

# from server.common.dependencies import get_db
from server.core.auth import schemas

router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    pass
