import requests

from configurations import *
from payloads import *
import configparser

from utilities import resources
from utilities.resources import *

# ADD Book
url = getconfig()['API']['endpoint']+apiresources.addBook
R = requests.post(url, json=payloadbodyADDBook('bcd12',334))
R_json = R.json()
print(R_json)
ID = R_json["ID"]
print(ID)
assert R_json['Msg'] == 'successfully added'


# DELETE Book
url_delete = getconfig()['API']['endpoint']+apiresources.deleteBook
R_Delete = requests.post(url_delete, json=payloadbodyDeleteBook())
R_DELETE_JSON = R_Delete.json()
print(R_DELETE_JSON)
msg = R_DELETE_JSON["msg"]
assert R_DELETE_JSON["msg"] == 'book is successfully deleted'