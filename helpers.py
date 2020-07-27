import pickle
from functools import reduce
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
