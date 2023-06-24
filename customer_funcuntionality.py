##Customer Service Functionality
from typing import Any, Text, Dict, List, Union

import Action, Tracker
import CollectingDispatcher
import FormAction


class ActionDigLaunch(Action):

    def name(self) -> Text:
        return "action_your_dig"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print(tracker.get_slot('dig'))


class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_info"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """required slots"""

        return ["User_Name", "DIG"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """required slots"""

        #template
        dispatcher.utter_message(template="utter_submit", name=tracker.get_slot('User_Name'),
                                 headset=tracker.get_slot('DIG'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """Dictionary"""

        return {
            "name": [self.from_entity(entity="User_Name", intent='my_name_is'),
                     self.from_text()],
            "headset": [self.from_entity(entity="DIG", intent="headset"),
                        self.from_text()],
        }



    def validate_dig(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """value"""
        print(value)
        if value.lower() in self.cuisine_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"DIG": value}
        else:
            print(value)
            dispatcher.utter_message(template="utter_wrong_value")
            # validation failed, set this slot to None
            return {"DIG": None}