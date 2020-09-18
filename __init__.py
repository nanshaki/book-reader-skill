from mycroft import MycroftSkill, intent_file_handler


class BookReader(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reader.book.intent')
    def handle_reader_book(self, message):
        self.speak_dialog('reader.book')


def create_skill():
    return BookReader()

