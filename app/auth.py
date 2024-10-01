from fastapi import Depends, HTTPException, Request
from app.session import get_session
from app.admin import get_user

redirect_to_login = HTTPException(
    status_code=307,
    headers={'Location': '/admin/login'}
)

async def get_current_user(request: Request):
    session_id = request.cookies.get("session_id")
    username = get_session(session_id)

    if username is None:
        raise redirect_to_login

    user = get_user(username)

    if not user:
        raise redirect_to_login
    return user


AuthenticatedUser = Depends(get_current_user)
