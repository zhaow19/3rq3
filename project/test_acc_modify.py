from project.account import Account


# The system shall allow customers, or delivery drivers to modify their account information after login.
# The system shall allow customers to change the information related to their customer accounts.

def user_login(input_userid, input_password):
    pass


def test_account_modify():
    accountinfo = Account()
    info = accountinfo.login()
    assert info(UserID=123456, passward="Aa123456")
    input_userid = [123456]
    input_password = ["Aa123456"]
    user_login(input_userid, input_password)
    if user_login == info():
        assert Account.acc_access == True, "Login successful, modification granted"
    else:
        assert Account.acc_access == False, "Login failed, modification denied"
