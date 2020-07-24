import pickle
from os import path


def loadCampaign(self, campaignID):
    if path.exists(f'/resources/campaign_{campaignID}.pickle'):
        with open(f'/resources/campaign_{campaignID}.pickle', "rb") as camp_file:
            campaign = pickle.load(camp_file)
