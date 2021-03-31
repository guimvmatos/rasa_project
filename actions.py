from typing import Any, Text, Dict, List, Union

from requests.exceptions import RequestException
from requests.models import Response

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

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

        dispatcher.utter_message("Obrigado pelas informações")
        return []