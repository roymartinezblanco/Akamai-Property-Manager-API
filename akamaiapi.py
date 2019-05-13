# -*- coding: utf-8 -*-
import requests, json, urllib, datetime, multiprocessing, argparse
from time import sleep
from urllib.parse import urljoin
from akamai.edgegrid import EdgeGridAuth


class Property:
    def __init__(self):
        self.accountId = ""
        self.contractid = ""
        self.assetId = ""
        self.groupid = ""
        self.propertyId = ""
        self.stagingVersion = 0
        self.productionVersion = 0
        self.baseVersion = 0
        self.latestVersion = 0
        self.newVersion = 0
        self.propertyName = ""
        self.baseVersionEtag = ""
        self.apiBaseUrl = ""
        self.apiRequest = requests.Session()
        self.data = object
        self.rules = dict
        self.error = False


def SearchProperty(pn: str, p: Property):
    postbody = '{"propertyName": "' + pn + '"}'
    outputurl = '/papi/v1/search/find-by-value'
    p.apiRequest
    result = p.apiRequest.post(urljoin(p.apiBaseUrl, outputurl), postbody, headers={"Content-Type": "application/json"})
    if result.status_code == 200:
        data = json.loads(json.dumps(result.json()))
        if data['versions']['items']:
            p.accountId = data['versions']['items'][0]['accountId']
            p.contractid = data['versions']['items'][0]['contractId']
            p.assetId = data['versions']['items'][0]['assetId']
            p.groupId = data['versions']['items'][0]['groupId']
            p.propertyId = data['versions']['items'][0]['propertyId']
            p.propertyName = data['versions']['items'][0]['propertyName']
            return p
    return None


def getconfig(p: Property):
    outputurl = '/papi/v1/properties/' + p.propertyId + '?contractId=' + p.contractid + '&groupId=' + p.groupId
    result = p.apiRequest.get(urljoin(p.apiBaseUrl, outputurl))
    var = result.headers['Location']
    data = json.loads(json.dumps(result.json()))
    return data


def getconfigver(p: Property):
    outputurl = '/papi/v1/properties/' + p.propertyId + '/versions/' + str(
        p.baseVersion) + '?contractId=' + p.contractid + '&groupId=' + p.groupId
    result = p.apiRequest.get(urljoin(p.apiBaseUrl, outputurl))
    data = json.loads(json.dumps(result.json()))
    p.baseVersionEtag = getetag(data)
    return


def getetag(d: dict):
    return d['versions']['items'][0]['etag']


def getConfigRules(p: Property):
    outputurl = '/papi/v1/properties/' + p.propertyId + '/versions/' + str(
        p.baseVersion) + '/rules?contractId=' + p.contractid + '&groupId=' + p.groupId + '&validateRules=true&validateMode=fast&dryRun=true'
    result = p.apiRequest.get(urljoin(p.apiBaseUrl, outputurl))
    p.rules = json.loads(json.dumps(result.json()))
    return


def getvarindex(p: Property, n: str, d: dict):
    i = 0
    index = -1
    for element in d['rules']['variables']:
        if element['name'] == n:
            index = i
            print('[' + str(
                datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": Variable "' + n + '" Found')
            break
        i = i + 1
    return index


def createVersion(p: Property):
    postbody = '{"createFromVersion": ' + str(p.baseVersion) + ',"createFromVersionEtag": "' + p.baseVersionEtag + '"}'
    outputurl = '/papi/v1/properties/' + p.propertyId + '/versions?contractId=' + p.contractid + '&groupId=' + p.groupId
    p.apiRequest.post(urljoin(p.apiBaseUrl, outputurl), postbody, headers={"Content-Type": "application/json"})
    return


def UpdateVariable(p: Property, vars: [], vals: []):
    i = 0
    for element in vars:
        varindex = getvarindex(p, element, p.rules)
        if varindex == -1:
            print('[' + str(
                datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": Error Variable "' + element + '" Not Found')
            p.error = True
            return
        else:
            p.rules['rules']['variables'][varindex]['value'] = vals[i]
        i = i + 1

    return p.rules


def UpdateConfig(p: Property):
    outputurl = '/papi/v1/properties/' + p.propertyId + '/versions/' + str(
        p.latestVersion) + '/rules?contractId=' + p.contractid + '&groupId=' + p.groupId + '&validateRules=false'
    del p.rules['propertyVersion']
    del p.rules['etag']
    del p.rules['warnings']
    p.rules['ruleFormat'] = 'v2018-02-27'
    result = p.apiRequest.put(urljoin(p.apiBaseUrl, outputurl), json.dumps(p.rules),
                              headers={"Content-Type": "application/json"})
    return result


def ActivateConfig(p: Property, env: str, note: str, email: str, warnings: object):
    postbody = {"propertyVersion": str(p.latestVersion), "network": env, "note": note, "notifyEmails": email,
                "acknowledgeWarnings": warnings, "useFastFallback": "false"}
    outputurl = '/papi/v1/properties/' + p.propertyId + '/activations?contractId=' + p.contractid + '&groupId=' + p.groupId
    result = p.apiRequest.post(urljoin(p.apiBaseUrl, outputurl), json.dumps(postbody),
                               headers={"Content-Type": "application/json"})
    data = json.loads(json.dumps(result.json()))
    if result.status_code == 400:
        if data["title"] == "Activation Warnings":
            warnings = []
            for element in data['warnings']:
                warnings.append(element['messageId'])

        if warnings is not None:
            a = ActivateConfig(p, env, note, email, warnings)
            return a
    elif result.status_code == 201:
        path = data['activationLink']
        url_parts = urllib.parse.urlparse(path)
        path_parts = url_parts[2].rpartition('/')
        return str(path_parts[2])

    return 'ERROR'


def GETActivation(p: Property, aID: str) -> object:
    outputurl = '/papi/v1/properties/' + p.propertyId + '/activations/' + aID + '?contractId=' + p.contractid + '&groupId=' + p.groupid
    result = p.apiRequest.get(urljoin(p.apiBaseUrl, outputurl))
    return result.json()


def MonitorActivation(p: Property, aID: str):
    while True:
        data = GETActivation(p, aID)
        status = data['activations']['items'][0]['status']

        if status == 'ACTIVE':
            print(
                '[' + str(datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '" Status: ' + status)
            break
        print('[' + str(
            datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '" Status: ' + status + '.... Trying again in 30s')
        sleep(30)
    return


def work(pn: str, baseEnv: str, activationtype: str, note: str, notify: str, variables: [], values: []):
    ''' [START] UPDATE CREDENTIALS HERE '''
    cs = "####################"                 #Client Secret
    host = "####################"               #Host
    at = "####################"                 #Access Token
    ct = "####################"                 #Client Token
    ''' [END] UPDATE CREDENTIALS HERE '''

    p = Property()
    p.apiBaseUrl = "https://" + host + "/"
    p.apiRequest.auth = EdgeGridAuth(
        client_token=ct,
        client_secret=cs,
        access_token=at
    )

    p = SearchProperty(pn, p)
    if p is None:
        print('[' + str(datetime.datetime.now()) + '] Configuration "' + pn + '" Not Found')
        return
    else:
        print('[' + str(
            datetime.datetime.now()) + '] Configuration "' + pn + '": Found with the id "' + p.propertyId + '"')
    p.data = getconfig(p)

    print('[' + str(datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '": Fetched')
    p.stagingVersion = p.data['properties']['items'][0]['stagingVersion']
    p.latestVersion = p.data['properties']['items'][0]['latestVersion']
    p.productionVersion = p.data['properties']['items'][0]['productionVersion']

    print('[' + str(datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": Latest Version: ' + str(
        p.latestVersion))

    print('[' + str(datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": Staging Version: ' + str(
        p.stagingVersion))
    print('[' + str(datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": production Version: ' + str(
        p.productionVersion))

    baseEnv = baseEnv.upper()
    if baseEnv == 'STAGING':
        p.baseVersion = p.stagingVersion
    elif baseEnv == 'PRODUCTION':
        p.baseVersion = p.productionVersion
    elif baseEnv == 'LASTEST':
        p.baseVersion = p.latestVersion
    else:
        print('[' + str(datetime.datetime.now()) + ']' + ' Invalid Environment provided')
        return
    getconfigver(p)

    print('[' + str(datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '": Base Version "' + str(
        p.baseVersion) + '" Etag: ' + p.baseVersionEtag)

    getConfigRules(p)

    createVersion(p)
    p.latestVersion = p.latestVersion + 1
    print('[' + str(
        datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": New version created, version number: ' + str(
        p.latestVersion))
    UpdateVariable(p, variables, values)
    if p.error == True:
        return

    print('[' + str(datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": Version "' + str(
        p.latestVersion) + '" Modified')
    UpdateConfig(p)

    print('[' + str(datetime.datetime.now()) + '] Configuration "' + p.propertyName + '": Rules uploaded')
    env = 'STAGING'
    if (activationType == 'STAGING') or (activationType == 'BOTH'):
        print('[' + str(
            datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '": Propagation Starting on: ' + env)
        activationID = ActivateConfig(p, env, note, notify, [])
        if activationID != 'ERROR':
            print('[' + str(
                datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '": Propagation Started on: ' + env)
            MonitorActivation(p, activationID)
        else:
            print('[' + str(
                datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '": Error Propagation on: ' + env)
            print('[' + str(datetime.datetime.now()) + ']' + ' Akamai OPEN END')
            return
    env = 'PRODUCTION'
    if (activationType == 'PRODUCTION') or (activationType == 'BOTH'):
        print('[' + str(
            datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '" Propagation Starting on: ' + env)
        print('[' + str(
            datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '" Propagation Started on: ' + env)
        activationID = ActivateConfig(p, env, note, notify, [])


        if activationID != 'ERROR':
            print('[' + str(
                datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '": Propagation Started on: ' + env)
            MonitorActivation(p, activationID)
        else:
            print('[' + str(
                datetime.datetime.now()) + ']' + ' Configuration "' + p.propertyName + '": Error Propagation Configuration on: ' + env)

    return


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Akamai OPEN Automation Script')
    parser.add_argument('-properties', nargs='+', type=str, help='<Required> List of configurations to update.',
                        required=True)
    parser.add_argument('-network', type=str, choices=['STAGING', 'PRODUCTION', 'BOTH', 'NONE'],
                        help='<Required> Akamai Network to Activate the configuration.', required=True)
    parser.add_argument('-baseline', type=str, choices=['PRODUCTION', 'STAGING'],
                        help='<Required> Configuration version to be used as the baseline. Production will be the only one allowed unless updated',
                        required=True)
    parser.add_argument('-emails', nargs='+', type=str, help='<Required> List of emails to be notified once activated.',
                        required=True)
    parser.add_argument('-note', type=str, help='<Required> Note to be used when activating the configuration.',
                        required=True)
    parser.add_argument('-variables', nargs='+', type=str, help='<Required> List of property variables to updated.',
                        required=True)
    parser.add_argument('-values', nargs='+', type=str, help='<Required> List of variable values to updated.',
                        required=True)
    args = vars(parser.parse_args())

    print('[' + str(datetime.datetime.now()) + ']' + '  Akamai OPEN START')
    configlist = args['properties']
    baseConfigEnv = args['baseline']
    activationType = args['network']
    note = args['note']
    notify = args['emails']
    variables = args['variables']
    values = args['values']

    if len(variables) == len(values):

        jobs = []

        for name in configlist:
            process = multiprocessing.Process(target=work,
                                              args=(str(name), baseConfigEnv, activationType, note, notify, variables,
                                                    values))
            jobs.append(process)
        for j in jobs:
            j.start()
        for j in jobs:
            j.join()
    else:
        print('[' + str(
            datetime.datetime.now()) + ']  Error: The number and order of variables have to match the number and order of the corresponding variable value.')

    print('[' + str(datetime.datetime.now()) + ']' + '  Akamai OPEN END')
