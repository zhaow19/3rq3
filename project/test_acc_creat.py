from project.account import AccountCreation,Account,SocialMediaAccount

#The system shall check if the contact information is valid.
def test_valid_account_creation():
    validaccount = [
        "165-654-4561",
        "aoweitru@gmail.com"
    ]
    account = AccountCreation
    for id in validaccount:
        assert account.account_creation(id) == True, "Valid account ID."

def test_invalid_account_creation():
    invalidaccount = [
        "***-***-****",
        "aoweitru@abc.com",
        None
    ]
    account = AccountCreation
    for id in invalidaccount:
        assert account.account_creation(id) == False, "Invalid account ID."

#The system shall check that the password a customer put is valid.
def test_valid_passward():
    validpassward = [
        "akjhgA4",
        "ahkjsg#E1",
        "5643EERTq"
    ]
    account = AccountCreation()
    for password in validpassward:
        assert account.account_creation(password) == True, "password should be verified as valid"

def test_invalid_passward():
    invalidpassward = [
        "akjhg",
        "GDSGFG",
        "123456",
        None
    ]
    account = AccountCreation()
    for password in invalidpassward:
        assert account.account_creation(password) == False, "password should not be verified, it is false"


#The system shall allow a customer, or a delivery driver to create an account with only one contact information and a password. The contact information can be a phone number or an email address.
def valid_ordinary_account_creation():
    if AccountCreation.account_creation == True:
        assert Account.Account == True, "User ID and user password acquired, ordinary creation successful"

def invalid_ordinary_account_creation():
    if AccountCreation.account_creation == False:
        assert Account.Account == False, "User ID or user password invalid, ordinary creation failed"

#The system shall allow customers and delivery drivers to create an account with their social media accounts.
def special_account_creation():
    AccountCreation.account_creation = SocialMediaAccount.Account
    assert Account.Account == True, "Social media account linked, special account creation successful"
