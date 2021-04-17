from os import P_OVERLAY
from typing import Any, Text, Dict, List, Union

import requests
import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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

        return [SlotSet("nome", nomef), SlotSet("email",emailf)]

class enviarBoleto(Action):
    def name(self):
        return "enviarBoleto"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        # conexão com os servidores do google
        smtp_ssl_host = 'smtp.office365.com'
        smtp_ssl_port = 587
        
        # username ou email para logar no servidor
        password = 'z4bbix@admin'

        sender = 'zabbix@feb.br'
        #receiver = ['guimvmatos@gmail.com','leonardo.dti@feb.br'] para enviar para mais de um destinatário
        #receiver = 'guimvmatos@gmail.com' para enviar para um destinatário
        receiver = tracker.get_slot("email")


        body = '''Prezado aluno(a), 
        Conforme solicitado, segue em anexo seu boleto'''

        #message = MIMEText('Hello World')
        message = MIMEMultipart()
        message['from'] = sender
        #message['to'] = ', '.join(receiver) para enviar para mais de um destinatário
        message['to'] = receiver
        message['subject'] = 'python script test'
        
        message.attach(MIMEText(body,'plain'))

        pdfname='pdf_sample_2.pdf'

        # open the file in bynary
        binarypdf = open(pdfname,'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binarypdf).read())
        
        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)

        #context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        session = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
        session.ehlo()
        #session.starttls(context=context)
        session.starttls()
        session.login(sender, password)
        session.sendmail(sender, receiver, message.as_string())
        session.quit()

        return []