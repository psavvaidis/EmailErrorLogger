import pickle
from campaign import Campaign
from os import path

class LogService:
    campaigns = []

    def __init__(self):
        self._gClient = self.connect()
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
