from project.account import AccountInfo

#The system shall check that the address a customer entered is a valid address in the system.
def test_valid_address():
    validaddress = [
        "1280 Main Street West, Hamilton, Ontario L8S 4L8"
    ]
    account = AccountInfo()
    for address in validaddress:
        assert account.Account_info(address) == True, "Address should be verified as valid"


def test_invalid_address():
    invalidaddress = [
        "sklfdhjgl",
        None
    ]
    account = AccountInfo()
    for address in invalidaddress:
        assert account.Account_info(address) == False, "Address should not be verified, it is false"
