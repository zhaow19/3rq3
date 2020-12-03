from project.account import Account

#The system shall save login information on mobile DIS application, so that customers do not have to log in every time they are using the DIS app.

def user_login(input_userid, input_password):
    pass


def test_saved_login():
    accountinfo = Account()
    info = accountinfo.login()
    assert info(UserID=123456, passward="Aa123456")
    input_userid = [123456]
    input_password = ["Aa123456"]
    user_login(input_userid, input_password)
    assert Account.save_login == Account.login , "login information saved."
