from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class HealthForm(FormAction):


    #Below that, define a new class for the form and pass in the FormAction method. Then, we define our first function, which returns the name of the form: health_form. The name function is required every time you create a form. You’ll recall health_form is the same form name we registered in the domain.yml file, and the action name we used in our stories—it’s important that the name matches in all of the places it’s referenced.
    def name(self):
        return "health_form"
    

    #Below the name function, we define a second function: required_slots. Like the name function, the required_slots function is required too. As the name suggests, it configures which slots are required by the form. In addition to specifying the required slots, we’re also introducing a bit of conditional logic. The first question we ask the user, “Did you exercise yesterday?,” is a yes or no question. If the user answers no, we don’t want to ask them what kind of exercise they did. Here, we’re telling the form that it should only require the exercise slot if confirm_exercise evaluates to True, otherwise, we’ll skip it.
    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot('confirm_exercise') == True:
            return ["confirm_exercise", "exercise", "sleep",
             "diet", "stress", "goal"]
        else:
            return ["confirm_exercise", "sleep",
             "diet", "stress", "goal"]
    

    #Next, create a third function: slot_mappings. This function is optional when creating a form. You need to map slots only if you don’t want to automatically fill slots with entities of the same name, and want to enforce some other logic.
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "confirm_exercise": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent="deny", value="None"),
            ],
            "diet": [
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny"),
            ],
            "goal": [
                self.from_text(intent="inform"),
            ],
        }
        #As you can see, we can provide multiple methods for filling a single slot. Take our first slot: confirm_exercise. There are a few ways a user could respond to “Did you exercise yesterday?” They could say “yes,” they could say “no,” or they could say “I went for a run,” which is essentially an affirmation. This gives us three possible intents that could fill the slot: affirm, intent, and inform. We also map the affirm/deny intents to values: True or False. This lets us create a boolean slot and use the value for conditional logic in our required_slots function. And as a side note, if the user says “I went for a run,” Rasa Open Source will extract the exercise entity and fill the exercise slot at the same time, and skip the follow-up question asking what kind of exercise they did.

        #With sleep, we could extract the sleep entity (e.g. “8 hours”), or the user could say None, which would match the deny intent. We map the deny intent to the value None, which is printed back to the user on form submission.

        #Another thing to note is the self.from_text() method. This method saves the full text of the user’s message to the slot. So if we ask “Did you stick to a healthy diet yesterday?” to fill the diet slot, we can capture a response like “way too much junk food.” We take the same approach for the goals slot, where we expect the user to enter a full statement like “I want to go to bed before 10pm.”
    

    #Finally, we create one last function: the submit function. This tells the assistant what to do when all of the slots in the form have been filled. In a more advanced assistant, you might want to do something like post data to a database or make an API call. Here, we’re going to keep things simple and utter a message: “Thanks, great job!”
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []