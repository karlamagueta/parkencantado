from fastapi import FastAPI, Form, HTTPException
from pydantic import EmailStr
from aiosmtplib import send
from email.message import EmailMessage
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("templates/index.html") as f:
        return f.read()

@app.post("/enviar-email/")
async def enviar_email(
    nome: str = Form(...),
    email: EmailStr = Form(...),
    telemovel: str = Form(...),
    data: str = Form(...),
    mensagem: str = Form(...),
):
    corpo_email = f"""
    Nome: {nome}
    E-mail: {email}
    Telemóvel: {telemovel}
    Data da Festa: {data}

    Mensagem:
    {mensagem}
    """

    logging.info(f"Dados recebidos: {nome}, {email}, {telemovel}, {data}, {mensagem}")

    message = EmailMessage()
    message["From"] = "testemailspython@gmail.com"
    message["To"] = "testemailspython@gmail.com"
    message["Subject"] = "Novo contato - Park Encantado"
    message.set_content(corpo_email)


    try:
        await send(
            message,
            hostname="smtp.gmail.com",
            port=587,
            use_tls=False,
            start_tls=True,
            username="testemailspython@gmail.com",
            password="zculsiepvnysbvrv",
        )
        logging.info("E-mail enviado com sucesso!")
        return {"message": "E-mail enviado com sucesso!"}
    except Exception as e:
        logging.error(f"Erro ao enviar e-mail: {e}")
        raise HTTPException(status_code=500, detail="Erro ao enviar o e-mail.")
