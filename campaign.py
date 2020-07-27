import pickle, json, random, time, helpers
import gmail_api.connect as gmail
from os import path
from gmail_api.utils.messages import *
from gmail_api.utils.labels import *

class Campaign:
    _id: int

    def __init__(self, title, sender, *recipients, message_subj=None, message_body=None):
        random.seed()
        self._id = random.randint(1, 100000000)
        self._title = title
        self._sender = sender
        self._recipients = recipients
        self._subject = message_subj
        self._body = message_body

    def __str__(self):
        return f'Campaign "{self._title}" with id {self._id}'

    def save(self):
        """
        Saves the campaign to a pickle file
        :return: null
        """
        try:
            with open(path.dirname(__file__) + f'/resources/campaign_{self._id}.pickle', "wb") as camp_file:
                pickle.dump(self, camp_file)
                return True
        except:
            return False

    def getID(self):
        return self._id

    def getTitle(self):
        return self._title

    def getBody(self):
        return self._body

    def getSubject(self):
        return self._subject

    def getSender(self):
        return self._sender

    def getRecipients(self):
        return self._recipients

    def updateSubject(self, subject):
        self._subject = subject

    def updateBody(self, body):
        self._body = body

    def updateTitle(self, title):
        self._title = title

    def updateSender(self, sender):
        self._sender = sender

    def addRecipients(self, recipients):
        for r in recipients:
            self._recipients.append(r)

    def setRecipients(self, recipients):
        self._recipients = []
        self._recipients.append(recipients)
