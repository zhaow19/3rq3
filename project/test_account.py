from project.account import AccountInfo

#The system shall verify the contact information before the customer, or the delivery driver can use the account.
def test_valid_contact_info():
    account = AccountInfo()
    valid_account_info = account.Account_info(contactinfo=True)

    assert valid_account_info == True, "contact information verified as valid."

def test_invalid_contact_info():
    account = AccountInfo()
    invalid_account_info = account.Account_info(contactinfo=False)

    assert invalid_account_info == True, "contact information verified as invalid."
