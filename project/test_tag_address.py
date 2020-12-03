from project.account import AccountInfo


#The system shall allow customers to put on a tag for each address.
def test_address_tag_work():
    tag = ["Work"]
    assert AccountInfo.Address(tag) == "Work", "Work tag set successfully for address."

def test_address_tag_Home():
    tag = ["Home"]
    assert AccountInfo.Address(tag) == "Home", "Home tag set successfully for address."
