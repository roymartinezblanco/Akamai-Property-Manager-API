# Akamai Property Manager API

This example was designed to update configurations that are active in the production and to update the variables provided and it will promote the changes to production, staging or both. It's meant to be a starting point to show how to edit [Akamai Delivery](https://www.akamai.com/) Configurations  using [Akamai-OPEN API's](https://developer.akamai.com/api) when [Akamai CLI](https://github.com/akamai/cli) is not an option.


### Functions in script
* Search configuration
* Fetch Configuration details
* Fetch Configuration Rules
* Update Configuration Rules
* Modify Variables
* Create Configuration Version
* Activate Configuration
* Monitor Activation of Configuration.

### Arguments:
```
-h, --help      Show allowed Arguments and values.
-properties     List of configurations to update. *
-network        Akamai Network to Activate the configuration. 
                Allowed Values: STAGING,PRODUCTION,BOTH,NONE *
-baseline       Configuration version to be used as the baseline.                      Production will be the only one allowed unless                         updated. 
                Allowed Values: Production, STAGING. *
-emails         List of emails to be once activated. *
-note           Note to be used when activating the configuration. *
-variables      List of property variables to updated. *
-values         List of variable values to updated. *
```
Note: * **Required argument.**


### Sample Run
Based on the Arguments above here is an example of how to execute this script.

```Shell
python akamaiapi.py -properties devops.somecompany.net -emails someone@somecompany.com -note "Sample Automation Script Run" -network STAGING -baseline PRODUCTION -variables PMUSER_EPS_ENABLED PMUSER_PSE_ENABLED -values FALSE FALSE
```
### Example Output
![Sample Run](https://raw.githubusercontent.com/roymartinezblanco/Akamai-Property-Manager-API/master/assets/scriptSampleRun.jpg)


## Prerequisites/Requirements

This are the liberies that you'll need to make sure it runs smoothly.

* requests
* json
* urllib
* datetime
* multiprocessing
* argparse
* time
* edgegrid

To run this script you will need python3 , pip3 and setuptools. Once pip3 and python3 are installed all additional dependencies are installed using the requierement.txt in the attachment provided.
```shell
pip3 install -r requirements.txt
```
If you don’t have python3 nor pip3 here are sample commands for Debian/Linux to get you to the wanted state.
```shell
apt-get install python3 python3-pip -y
python3 -m pip install setuptools
pip3 install -r requirements.txt
```


## Disclaimer
**Keep in mind that is meant to be a sample script to build on top of, it is functional but it by no means cover every single scenario.**

# License

I am providing code and resources in this repository to you under an open source license. Because this is my personal repository, the license you receive to my code and resources is from me and not my employer (Akamai).

```
Copyright 2019 Roy Martinez

Creative Commons Attribution 4.0 International License (CC BY 4.0)

http://creativecommons.org/licenses/by/4.0/
```
