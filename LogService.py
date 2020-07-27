import pickle, helpers
import exceptions as e
from campaign import Campaign
from os import path
from gmail_api.connect import *
from gmail_api.utils.messages import *
from gmail_api.utils.labels import *

class LogService:
    campaigns = []

    def __init__(self):
        self._gClient = connect()
        self.campaigns = self.loadCampaigns()

    def __str__(self):
        return "Log Service"

    def createCampaign(self, title, sender, recipients, subj, body):
        newCampaign = Campaign(title, sender, recipients, message_subj=subj, message_body=body)

        while newCampaign.getID() in self.campaigns:
            newCampaign = Campaign(title, sender, recipients, message_subj=subj, message_body=body)

        return newCampaign

    def save(self):
        with open(f'/resources/campaigns.pickle', "wb") as camp_file:
            pickle.dump(self.campaigns, camp_file)

        for campaign in self.campaigns:
            campaign.save()

    def loadCampaigns(self):
        if path.exists('/resources/campaigns.pickle'):
            with open('/resources/campaigns.pickle', "rb") as camp_file:
                return pickle.load(camp_file)
        else:
            return []

    def log(self, campaign, *msg_params):
        """
        Sends the message

        First, the message is constructed by combining the default campaign message and the message args
        Then, it sends the message through the GMAIL API

        :param campaign: the current campaign sending the message for
        :param msg_params: unknown number of message parameters
        :return: success or failure feedback
        """

        body_text = helpers.buildText(campaign.getBody(), msg_params)

        try:
            message = CreateMessage(campaign.getSender(), campaign.getRecipients(), campaign.getSubject(), body_text)
            SendMessage(self._gClient, 'me', message)
            print('Message Sent Successfully')
            return True
        except e.WrongNumberOfArguments as err:
            print(f'Sending message failed - {err}')
        except:
            print('Sending message failed - Unknown error occurred')
        finally:
            return False
