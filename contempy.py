#!/usr/bin/env python
import os
import time

class ContempFile():
    def __init__(self, session_name, filepath):
        self.filepath = os.path.abspath(filepath)
        self.session = session_name

    def start(self):
        with open(self.filepath, 'w') as file:
            file.write(self.generate_start_block())

    def end(self):
        with open(self.filepath, 'a') as file:
            file.write(self.generate_end_block())

    def generate_start_block(self):
        output = "SESSION: " + self.session + " | "
        output = output + "SESSION STARTED: " + time.strftime("%c")
        output = output + "\n"
        return output

    def generate_end_block(self):
        output = "\n\n\n"
        output = output + "SESSION: " +  self.session + " | "
        output = output + "SESSION ENDED: " + time.strftime("%c")
        return output

    def add_item(self, item_text):
        with open(self.filepath, 'a') as file:
            message = "\n\n"
            message = message + "[" + time.strftime("%c") + "]\n"
            message = message + item_text
            file.write(message)


if __name__=='__main__':
    print "Welecome to contempy.py!\n"
    session_name = raw_input("Enter the name for this notes session > ")
    filepath = raw_input("Enter the filename for the notes file > ")

    print "Note taking has begun! Enter your note at the prompt and press enter to commit it. Type '==EXIT==' when you're finished."

    note = ""
    file = ContempFile(session_name, filepath)
    file.start()
    while note != "==EXIT==":
        note = raw_input("> ")
        if note != '==EXIT==':
            file.add_item(note)

    file.end()
