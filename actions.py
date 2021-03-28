# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class AlunoForm(FormAction):

    def name(self): #deve retornar o nome do form, conforme esta em domain.yml
        return "aluno_form"

    @staticmethod
    def required_slots(tracker): #slots que deve ser preenchidos antes do metodo submit() ser invocado

        if tracker.get_slot("nome") != "":
            return ["nome", "ra", "email", "celular"]
        else:
            return ["ra", "email", "celular"]

    def submit (
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any],
    ) -> List[Dict]:
        return []        


    def slot_mappings(self) -> dict[Text, Union[Dict, List[Dict]]]:
        return {
            "nome":[
                self.from_entity(entity="nome")
            ],  
            "ra":[
                self.from_entity(entity="ra")
            ],
            "email":[
                self.from_entity(entity="email")
            ],
            "celular":[
                self.from_entity(entity="celular")
            ]
        }