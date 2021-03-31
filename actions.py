from typing import Any, Text, Dict, List, Union

from requests.exceptions import RequestException
from requests.models import Response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

import requests
import json
import os
airtable_api_key="keyK64wVMeF2p7Hfj"
base_id="appioQOpy9VguaEQq"
table_name="Table%201"

def log_atendimento(nome, ra, have_email, email, telefone):
    request_url=f"https://api.airtable.com/v0/{base_id}/{table_name}"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {airtable_api_key}",
    } 

    data = {
        "fields": {
            "ra": ra,
            "nome": nome,
            "have_email": have_email,
            "email": email,
            "telefone": telefone,
        }
    }
    try:
        response = requests.post(
            request_url, headers=headers, data=json.dumps(data)
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    return response
    print(response.status_code)

class HealthForm(FormAction):

    def name(self):
        return "aluno_form"
    
    @staticmethod
    def required_slots(tracker):

        return ["nome", "ra", "have_email", "email","telefone"]
       
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "nome": [
                self.from_text(intent="inform"),
                self.from_entity(entity="nome"),
            ],
            "ra": [
                self.from_text(intent="inform"),
                self.from_entity(entity="ra"),
            ],
            "have_email":[
                self.from_entity(entity="have_email"),
                self.from_intent(intent="affirm",value=True),
                self.from_intent(intent="deny",value= False),
            ],
            "email": [
                self.from_text(intent="inform"),
                self.from_entity(entity="email"),
            ],
            "telefone": [
                self.from_text(intent="inform"),
                self.from_entity(entity="telefone"),
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        nome = tracker.get_slot("nome"),
        ra = tracker.get_slot("ra"),
        have_email = tracker.get_slot("have_email"),
        email = tracker.get_slot("email"),
        telefone = tracker.get_slot("telefone")

        response = log_atendimento(
            nome=nome,
            ra=ra,
            have_email=have_email,
            email=email,
            telefone=telefone
        )

        dispatcher.utter_message("Obrigado pelas informações.Elas foram salvas")
        return []