import requests


def after_scenario(context, scenario):

    DELETE_response = requests.post('http://216.10.245.166/Library/DeleteBook.php',json={"ID" :context.ID})
    DELETE_JSON = DELETE_response.json()
    print(DELETE_JSON)
    msg = DELETE_JSON["msg"]
    assert DELETE_JSON["msg"] == 'book is successfully deleted'

