from fastapi import Depends, HTTPException, Request
from app.session import get_session
from starlette.responses import RedirectResponse
from app.session import session_conn


redirect_to_login = HTTPException(
    status_code=307,
    headers={'Location': '/admin/login'}
)

def get_current_user(request: Request):
    session_id = request.cookies.get("session_id")
    username = get_session(session_id)

    if username is None:
        raise redirect_to_login

    db = session_conn()
    cursor = db.cursor()

    cursor.execute("""\
        SELECT * FROM users WHERE username = ?""",
        (username,)
    )
    user = cursor.fetchone()
    db.close()

    if not user:
        raise redirect_to_login
    return user[0]


AuthenticatedUser = Depends(get_current_user)
