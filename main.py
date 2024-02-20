import os
import smtplib
import sqlite3
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


def enviar_email(destinatario, assunto, mensagem):

    smtp_host = 'smtp.gmail.com'
    smtp_port = 587

    usuario = os.getenv('EMAIL_USUARIO')
    senha = os.getenv('EMAIL_SENHA')

    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(usuario, senha)

        server.send_message(msg)
        print("E-mail enviado com sucesso!")


conn = sqlite3.connect('dados.db')
c = conn.cursor()
c.execute('SELECT nome, segundo_email FROM usuarios')

for row in c.fetchall():
    nome = row[0]
    email = row[1]
    assunto = 'Teste de envio de e-mail com Python e Gmail'
    mensagem = f'Olá {nome}, este é um e-mail enviado através de Python usando o Gmail!'
    enviar_email(email, assunto, mensagem)

# destinatario = 'lolfirmino13@gmail.com'
# assunto = 'Assunto do e-mail'
# mensagem = 'Olá, este é um e-mail enviado através de Python usando o Gmail!'
# enviar_email(destinatario, assunto, mensagem)
