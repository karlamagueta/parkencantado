import logging
from email.message import EmailMessage

import arel
import jinja2
from aiosmtplib import send
from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import EmailStr

from .config import settings
from .utils import NoCacheStaticFiles

logging.basicConfig(level=logging.INFO)

DEBUG = settings.get("DEBUG") is True

app = FastAPI()

if DEBUG:
    static_class = NoCacheStaticFiles
    logging.info("Uncached static files")
else:
    static_class = StaticFiles

app.mount(
    "/static",
    static_class(directory=settings.path_for("static")),
    name="static",
)

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(settings.path_for("templates")),
    autoescape=True,
)
templates = Jinja2Templates(env=jinja_env)


if DEBUG:
    # Auto reload front-end when template changes
    hot_reload = arel.HotReload(
        paths=[
            arel.Path(settings.path_for("templates")),
            arel.Path(settings.path_for("static")),
        ]
    )
    app.add_websocket_route("/hot-reload", route=hot_reload, name="hot-reload")
    app.add_event_handler("startup", hot_reload.startup)
    app.add_event_handler("shutdown", hot_reload.shutdown)
    templates.env.globals["DEBUG"] = True
    templates.env.globals["hot_reload"] = hot_reload


@app.get("/{path}", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request, path: str = "index"):
    return templates.TemplateResponse(
        request=request, name=f"{path}.html", context={}
    )


@app.get("/admin", response_class=HTMLResponse)
async def read_index(request: Request, path: str = "admin"):
    return templates.TemplateResponse(
        request=request, name="admin.html", context={}
    )


@app.post("/enviar-email/")
async def enviar_email(
    nome: str = Form(...),
    email: EmailStr = Form(...),
    telemovel: str = Form(...),
    data: str = Form(...),
    mensagem: str = Form(...),
):
    corpo_email = (
        jinja_env.get_template("email/contato.html")
        .render(
            preview_text=f"Novo email de {nome}",
            nome=nome,
            email=email,
            telemovel=telemovel,
            data=data,
            mensagem=mensagem,
        )
        .encode("utf-8")
    )

    logging.info(
        f"Dados recebidos: {nome}, {email}, {telemovel}, {data}, {mensagem}"
    )

    message = EmailMessage()
    message["From"] = settings.from_address
    message["To"] = settings.to_address
    message["Subject"] = f"Novo contato - {nome} - {settings.site_name}"
    message.add_header("Content-Type", "text/html")
    message.set_payload(corpo_email)

    try:
        await send(message, **settings.email_options)
        logging.info("E-mail recebido com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao enviar e-mail: {e}")
        raise HTTPException(status_code=500, detail="Erro ao enviar o e-mail.")
    else:
        # Confirmation to the sender
        confirmation_message = EmailMessage()
        confirmation_message["From"] = settings.from_address
        confirmation_message["To"] = email
        confirmation_message["Subject"] = (
            f"Recebemos a sua mensagem - {settings.site_name}"
        )
        confirmation_message.add_header("Content-Type", "text/html")
        confirmation_message.set_payload(
            jinja_env.get_template("email/confirmation.html")
            .render(
                preview_text=f"Ola {nome} recebemos a sua mensagem.",
                nome=nome,
                data=data,
            )
            .encode("utf-8")
        )
        await send(confirmation_message, **settings.email_options)
        logging.info("Confirmacao enviada com sucesso!")

    return {"message": "E-mail enviado com sucesso!"}

@app.post("/enviar-email-contacto/")
async def enviar_email_contacto(
    nome_contacto: str = Form(...),
    email_contacto: EmailStr = Form(...),
    telemovel_contacto: str = Form(...),
    mensagem_contacto: str = Form(...),
):
    corpo_email = (
        jinja_env.get_template("email/contato.html")
        .render(
            preview_text=f"Novo email de {nome_contacto}",
            nome_contacto=nome_contacto,
            email_contacto=email_contacto,
            telemovel_contacto=telemovel_contacto,
            mensagem_contacto=mensagem_contacto,
        )
        .encode("utf-8")
    )

    logging.info(
        f"Dados recebidos: {nome_contacto}, {email_contacto}, {telemovel_contacto}, {mensagem_contacto}"
    )

    message = EmailMessage()
    message["From"] = settings.from_address
    message["To"] = settings.to_address
    message["Subject"] = f"Novo contato - {nome_contacto} - {settings.site_name}"
    message.add_header("Content-Type", "text/html")
    message.set_payload(corpo_email)

    try:
        await send(message, **settings.email_options)
        logging.info("E-mail recebido com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao enviar e-mail: {e}")
        raise HTTPException(status_code=500, detail="Erro ao enviar o e-mail.")
    else:
        # Confirmation to the sender
        confirmation_message = EmailMessage()
        confirmation_message["From"] = settings.from_address
        confirmation_message["To"] = email_contacto
        confirmation_message["Subject"] = (
            f"Recebemos a sua mensagem - {settings.site_name}"
        )
        confirmation_message.add_header("Content-Type", "text/html")
        confirmation_message.set_payload(
            jinja_env.get_template("email/confirmation.html")
            .render(
                preview_text=f"Ola {nome_contacto} recebemos a sua mensagem.",
                nome=nome_contacto,
            )
            .encode("utf-8")
        )
        await send(confirmation_message, **settings.email_options)
        logging.info("Confirmacao enviada com sucesso!")

    return {"message": "E-mail enviado com sucesso!"}
