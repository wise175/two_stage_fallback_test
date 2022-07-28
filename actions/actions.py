from typing import Text, Dict, Any, List

from rasa.shared.core.constants import ACTION_DEFAULT_ASK_AFFIRMATION_NAME, \
    ACTION_DEFAULT_FALLBACK_NAME
from rasa_sdk import Action, Tracker
from rasa_sdk.events import ConversationPaused, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher


class ActionDefaultAskAffirmation(Action):
    """
        Overwrite ask affirmation action
    """

    def name(self) -> Text:
        return ACTION_DEFAULT_ASK_AFFIRMATION_NAME

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        latest_message = tracker.latest_message
        if latest_message is None:
            raise TypeError(
                "Cannot find last user message for detecting fallback "
                "affirmation."
            )

        dispatcher.utter_message(response="utter_ask_rephrase")
        return []


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return ACTION_DEFAULT_FALLBACK_NAME

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_default")
        return [ConversationPaused(), UserUtteranceReverted()]
