import requests
import json
import base64
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

def load_config():
    with open('Postman.ionapi') as json_file:
        data = json.load(json_file)

    return data 

def login(config):

    

    base_url = ''
    url = base_url + ""

    data = {
                'grant_type' : 'password',
                'username' : config['saak'],
                'password' : config['sask'],
                'client_id' : config['ci'],
                'client_secret' : config['cs'],
                'scope' : '',
                'redirect_uri' : 'https://localhost/'
    }

    r = requests.post(url, data=data)
    
    return r.json()

def header(config,token):
    '''
        headers = {
        'Content-Type': 'application/json',
        'X-TenantId': '',
        'X-ClientId': '',
        'Authorization': '',
        'User-Agent': '',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'Postman-Token': '',
        'Host': 'mingle-ionapi.inforcloudsuite.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Length': '359',
        'Cookie': '',
        'Connection': 'keep-alive'
        }
    '''

    headers = {
        'Content-Type':         'application/json',
        'X-TenantId':           config['ti'],
        'Connection':           'keep-alive',
        'Host':                 'mingle-ionapi.inforcloudsuite.com',
        'Accept-Encoding':      'gzip, deflate, br',
        'Cache-Control':        'no-cache',
        'User-Agent':           '',
        'X-ClientId':           config['ci'],
        'Accept':               '*/*',
        'Authorization':        'Bearer ' +token['access_token'],

    }
    return headers

