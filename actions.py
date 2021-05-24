from os import P_OVERLAY
from typing import Any, Text, Dict, List, Union
import typing_extensions

import requests
import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email import *

from requests.exceptions import RequestException
from requests.structures import CaseInsensitiveDict
from requests.models import Response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher, Action
from rasa_sdk.forms import FormAction
from rasa_sdk.events import AllSlotsReset, SlotSet



class AlunoForm(FormAction):

    def name(self):
        return "aluno_form"
    
    @staticmethod
    def required_slots(tracker):

        return ["ra"]
       
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {

            "ra": [
                self.from_text(intent="ra"),
                self.from_entity(entity="ra"),
            ],
        }
        
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        dispatcher.utter_message("Te encontrei!")
        return []


class dadosAluno(Action):
    def name(self):
        return "dadosAluno"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        request_url=f"http://api.feb.br/RM_Controller_Central/getAluno"
    
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Accept"] = "application/json"
        
        ra_aluno = tracker.get_slot("ra")
        data = "ra=%s" % (ra_aluno)
        response = requests.post(
                request_url, headers=headers, data=data
            )
        
        reply=response.json()
        raf=reply['ra']
        nomef=reply['nome_completo']
        celularf=reply['celular']
        emailf=reply['email']
        #input = tracker.latest_message["text"]
        #print(input)
        return [SlotSet("nome", nomef), SlotSet("email",emailf)]

class handoverAction(Action):
    def name(self) -> Text:
        return "handoverAction"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Accept"] = "application/json"

        INCOMING_ENDPOINT_URL = "https://unifeb.rocket.chat/api/apps/public/646b8e7d-f1e1-419e-9478-10d0f5bc74d9/incoming"

        payload = {
            "action": "handover",
            "sessionId": tracker.sender_id,
            "actionData": {
              "targetDepartment": "Test Bot2"
            }
        }
        
        response = requests.post(INCOMING_ENDPOINT_URL, headers=headers, data=payload)
        print('Handover Endpoint response', response.content)

        return []

class closeChatAction(Action):
    def name(self) -> Text:
        return "closeChatAction"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Accept"] = "application/json"

        INCOMING_ENDPOINT_URL = "https://unifeb.rocket.chat/api/apps/public/646b8e7d-f1e1-419e-9478-10d0f5bc74d9/incoming"

        payload = {
            "action": "close-chat",
            "sessionId": tracker.sender_id
        }
        
        response = requests.post(INCOMING_ENDPOINT_URL, headers=headers, data=payload)
        print('Handover Endpoint response', response.content)

        return []

class enviarBoleto(Action):
    def name(self):
        return "enviarBoleto"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # conexão com os servidores da MS
        smtp_ssl_host = 'smtp.office365.com'
        smtp_ssl_port = 587
        
        # username ou email para logar no servidor
        #password = 'z4bbix@admin'
        #sender = 'zabbix@feb.br'
        #receiver = ['guimvmatos@gmail.com','leonardo.dti@feb.br'] para enviar para mais de um destinatário
        #receiver = 'guimvmatos@gmail.com' para enviar para um destinatário

        password = 'Unifeb@2021'
        sender = 'relacionamento@feb.br'
        receiver = tracker.get_slot("email")
        nome = tracker.get_slot("nome")
        
        body1 = "Olá %s, \n\n Conforme solicitado, segue em anexo seu boleto para pagamento. \n\n" % (nome)

        body2="""
        <html>
        <head></head>
            <body>
                <p>Caso as informa&ccedil;&otilde;es estejam erradas, voc&ecirc; pode realizar o contato on-line <a href="https://unifeb.rocket.chat/livechat?mode=popout">clicando aqui</a>. Voc&ecirc; ser&aacute; redirecionado para nosso suporte via CHAT. Voc&ecirc; pode come&ccedil;ar se identificando e dizendo qual &eacute; o seu problema. Nossa equipe estar&aacute; &agrave; disposi&ccedil;&atilde;o para lhe ajudar.</p>

                <p><a href="https://unifeb.rocket.chat/livechat?mode=popout" target="_blank"><img src="images/livechat.jpg"/></a></p>
                
                <p>Caso o link n&atilde;o funcione, acesse <a href="www.unifeb.edu.br">www.unifeb.edu.br</a> e procure pelo &iacute;cone de chat no canto inferior direito da tela. Ao clicar no &iacute;cone, o chat j&aacute; estar&aacute; dispon&iacute;vel para voc&ecirc;.</p>
                
                <p>Nosso suporte est&aacute; dispon&iacute;vel de segunda a sexta feira, das 9h &agrave;s 19h, e s&aacute;bado das 9h &agrave;s 11h.</p>
            </body>
        </html>
        """
        #primeira parte: colocando o body (plain+html)
        msg_alternative = MIMEMultipart('alternative')
        msg_alternative.attach(MIMEText(body1,'plain'))
        msg_alternative.attach(MIMEText(body2, 'html'))

        #segunda parte: setando o anexo .pdf
        pdfname='pdf_sample_2.pdf'
        binarypdf = open(pdfname,'rb')
        #attachment = email.mime.application.MIMEApplication(binarypdf.read(),_subtype="pdf")
        attachment = MIMEApplication(binarypdf.read(),_subtype="pdf")
        binarypdf.close()
        attachment.add_header('Content-Disposition', 'attachment', filename=pdfname)

        #terceira parte: criando modo mixo
        msg_mixed = MIMEMultipart('mixed')
        msg_mixed.attach(msg_alternative)
        msg_mixed.attach(attachment)
        msg_mixed['from'] = sender
        #msg_mixed['to'] = ', '.join(receiver) para enviar para mais de um destinatário
        msg_mixed['to'] = receiver
        msg_mixed['subject'] = 'Boleto UNIFEB'

        #quarta parte: conectando e enviando
        session = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
        session.ehlo()
        #session.starttls(context=context)
        session.starttls()
        session.login(sender, password)
        session.sendmail(sender, receiver, msg_mixed.as_string())
        session.quit()

        return []

'''
        #message = MIMEText('Hello World')
        message = MIMEMultipart('relative')
        message['from'] = sender
        #message['to'] = ', '.join(receiver) para enviar para mais de um destinatário
        message['to'] = receiver
        message['subject'] = 'Boleto UNIFEB'
        
        message.attach(MIMEText(body1,'plain'))
        message.attach(MIMEText(body2,'html'))

        pdfname='pdf_sample_2.pdf'

        # open the file in bynary
        binarypdf = open(pdfname,'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binarypdf).read())
        
        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        payload.add_header('Content-decomposition', 'attachment', filename="boleto.pdf")
        message.attach(payload)

        #context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        session = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
        session.ehlo()
        #session.starttls(context=context)
        session.starttls()
        session.login(sender, password)
        session.sendmail(sender, receiver, message.as_string())
        session.quit()
'''
        
