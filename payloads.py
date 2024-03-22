def payloadbodyADDBook(isbn,aisle):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }
    return body

def payloadbodyDeleteBook():
    Del_body = {"ID": "bcd12227"}
    return Del_body
