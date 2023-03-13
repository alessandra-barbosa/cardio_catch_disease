# Requests to API and return prediction

from requests import post
import json
from .views import 

def request_api():
    data = data_input

    #API request
    url = "https://ccd-model.herokuapp.com/ccd/predict"
    header = {"Content-type":'application/json'}
    response_ccd = requests.post(url, data=data, headers=header)
    df_response = pd.DataFrame(response_ccd.json(), columns=response_ccd.json()[0].keys())

return df_response