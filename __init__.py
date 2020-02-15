from mycroft import MycroftSkill, intent_file_handler


class Karma(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('karma.intent')
    def handle_karma(self, message):
        self.speak_dialog('karma')


def create_skill():
    return Karma()

