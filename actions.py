from typing import Any, Text, Dict, List, Union

import requests
import json

from requests.exceptions import RequestException
from requests.structures import CaseInsensitiveDict
from requests.models import Response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
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
        


    def buscarDadosAluno(self,ra_aluno):
        request_url=f"http://api.feb.br/RM_Controller_Central/getAluno"
    
        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        headers["Accept"] = "application/json"
        
        data = "ra=%s" % (ra_aluno)
        response = requests.post(
                request_url, headers=headers, data=data
            )
        
        reply=response.json()
        raf=reply['ra']
        nomef=reply['nome_completo']
        celularf=reply['celular']
        emailf=reply['email']
        {"nome": nomef}
        {"email": emailf}

        #return raf,nomef,emailf
        return [SlotSet("nome": nomef, SlotSet("email":emailf)]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        
        
        dispatcher.utter_message("Obrigado pelas informações")
        return []