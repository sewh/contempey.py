#!/usr/bin/env python
import os
import time

class ContempFile():
    def __init__(self, file_path, starts_at, initials):
        self.filepath = os.path.abspath(file_path)
        self.starts_at = int(starts_at)    # The note increment
        self.initials = initials
        
    def init_file(self):
        with open(self.filepath, 'a') as open_file:
            open_file.write(self.create_start_session())
    
    def finish_file(self):
        with open(self.filepath, 'a') as open_file:
            open_file.write(self.create_end_session())        
    
    def add_note(self, evidence_id, message):
        number = "N%.3d" % (self.starts_at)
        self.starts_at += 1
        
        first_line = "[{0}: {1}: {2}]".format(number, self.initials, evidence_id)
        second_line = message + "\n\n"
        
        output = first_line + "\n" + second_line
        
        with open(self.filepath, 'a') as open_file:
            open_file.write(output)
    
    def create_date_string(self):
        """
        Must have the format 2010-04-12 22:15
        """
        now = time.localtime()
        return time.strftime("%Y-%m-%d %H:%M", now)
    
    def create_start_session(self):
        """
        Must have format [SESSION START: 2010-04-12 22:15]
        """
        now = self.create_date_string()
        return "[SESSION START: " + now + "]\n"
    
    def create_end_session(self):
        """
        Must have format [SESSION END: 2010-04-12 22:15]
        """
        now = self.create_date_string()
        return "[SESSION END: " + now + "]\n"  
    
    
    
if __name__=='__main__':
    print "Welcome to contempy.py!"
    filename = raw_input("Contemporaneous file location > ")
    starts_at = raw_input("What message number should we start at? > ")
    initials = raw_input("Please enter your initials > ")
    
    print "Prompt is starting. Enter ==EXIT== at the message prompt to close the session."
    
    # Main loop
    file = ContempFile(filename, starts_at, initials)
    file.init_file()
    while True:
        evidence_ref = raw_input("Evidence ID > ")
        message = raw_input("Message > ")

        if evidence_ref == "==EXIT==" or message == "==EXIT==":
            print "Exiting. Thank you!"
            break

        print "Are you sure you want to commit:"
        print "Evidence Reference: " + evidence_ref
        print "Message: " + message
        should_commit = raw_input("YES or NO? ")
        
        if should_commit == "YES":
            file.add_note(evidence_ref, message)
        
    file.finish_file()
    print "Done! Thank you!"
