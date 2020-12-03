from project.account import AccountInfo

#The system shall allow customers, or delivery drivers to view their account information.
def test_view_info():
    account = AccountInfo()
    information = account.Account_info
    assert information == AccountInfo.Account_info, "The system should return account information"
