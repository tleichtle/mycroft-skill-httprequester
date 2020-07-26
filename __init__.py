# Copyright 2020 Thomas Leichtle.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class HttpRequesterSkill(MycroftSkill):
    def __init__(self):
        super(TemplateSkill, self).__init__(name="HttpRequesterSkill")
        self.count = 0

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("BeamerIntent").require("BeamerKeyword"))
    def handle_beamer_intent(self, message):
        self.speak("starting beamer")
        url = 'http://192.168.1.138/ir?code=0xc1aa09f6&bits=32&protocol=NEC'
        r = requests.get(url)
        self.speak("command was executed")

    #@intent_handler(IntentBuilder("").require("Count").require("Dir"))
    #def handle_count_intent(self, message):
    #    if message.data["Dir"] == "up":
    #        self.count += 1
    #    else:  # assume "down"
    #        self.count -= 1
    #    self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False


def create_skill():
    return HttpRequesterSkill()
