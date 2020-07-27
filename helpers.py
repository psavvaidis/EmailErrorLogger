import pickle
from functools import reduce
from os import path
import re

from exceptions import WrongNumberOfArguments


def loadCampaign(self, campaignID):
    if path.exists(f'/resources/campaign_{campaignID}.pickle'):
        with open(f'/resources/campaign_{campaignID}.pickle', "rb") as camp_file:
            campaign = pickle.load(camp_file)


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
