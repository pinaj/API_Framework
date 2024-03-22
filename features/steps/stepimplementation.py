import requests
from behave import *

from configurations import *
from payloads import *
from utilities.resources import *


@given("the books details which neeed to be added")
def steep_impl(context):
    context.url = getconfig()['API']['endpoint'] + apiresources.addBook
    context.payload = payloadbodyADDBook('bcd12p','334')

@when('when the AddBook post api is being executed')
def step_impl(context):
    context.R = requests.post(context.url, json=context.payload)


@then('the book is successfully added')
def step_impl(context):
    R_json = context.R.json()
    print(R_json)
    context.ID = R_json["ID"]
    print(context.ID)
    assert R_json['Msg'] == 'successfully added'


@given("the books details with {isbn} and {aisle}")
def steep_impl(context,isbn,aisle):
    context.url = getconfig()['API']['endpoint'] + apiresources.addBook
    context.payload = payloadbodyADDBook(isbn,aisle)