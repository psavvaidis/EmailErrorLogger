import pickle
from os import path
import re

from exceptions import WrongNumberOfArguments


def loadCampaign(campaignID):
    if path.exists(path.dirname(__file__) + f'/resources/campaign_{campaignID}.pickle'):
        with open(path.dirname(__file__) + f'/resources/campaign_{campaignID}.pickle', "rb") as camp_file:
            campaign = pickle.load(camp_file)
            return campaign
    return None


def loadCampaigns():
    if path.exists(path.dirname(__file__) + '/resources/campaigns.pickle'):
        with open(path.dirname(__file__) + '/resources/campaigns.pickle', "rb") as camp_file:
            return pickle.load(camp_file)
    else:
        return []


def buildText(text, *txt_args, param_prefix='@'):
    params = []

    # Extracting and striping white spaces from params
    for param, arg in re.findall(r'((^| )' + param_prefix + '\w+)', text):
        param = re.sub(" ", "", param)
        params.append(param)

    if not len(params) == len(txt_args):
        raise WrongNumberOfArguments(f'{len(params)} argument(s) expected ({params})')

    for index, arg in enumerate(txt_args):
        text = text.replace(params[index], arg)

    return text


def updateCampaign(campaign, title=None, sender=None, recipients=None, subject=None, body=None):
    campaign.updateTitle(title) if title else None
    campaign.updateSender(sender) if sender else None
    campaign.addRecipients(recipients) if recipients else None
    campaign.updateSubject(subject) if subject else None
    campaign.updateBody(body) if body else None
