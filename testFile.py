# https://pypi.org/project/CoWIN-API-by-Kunal-Kumar-Sahoo/
import requests
import json


from cowin_api import CoWinAPI

# district_id = '97'
# date = '06-06-2021'
# min_age_limit = 18
#
# cowin = CoWinAPI()
# available_centers = cowin.get_availability_by_district(district_id)
# print(json.dumps(available_centers, sort_keys=True, indent=4))

# from cowin_api import CoWinAPI
#
pin_code = "800001"
date = '06-06-2021'  # Optional. Default value is today's date
min_age_limit = 45  # Optional. By default returns centers without filtering by min_age_limit

cowin = CoWinAPI()
available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
#print(json.dumps(available_centers, sort_keys=True, indent=4))

cowin = CoWinAPI()
states = cowin.get_states()
#print(json.dumps(states, sort_keys=True, indent=4))

state_id = '5'
cowin = CoWinAPI()
districts = cowin.get_districts(state_id)
print(json.dumps(districts, sort_keys=True, indent=4))