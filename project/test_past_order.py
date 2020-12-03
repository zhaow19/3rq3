from project.account import OrderHistory, Account

#The system shall allow customers to check their past orders after login.

def test_order_history():

    if Account.acc_access ==  True:
        assert OrderHistory.Access_Past_Order == True, "access for past order granted"
    if Account.acc_access == False:
        assert OrderHistory.Access_Past_Order == False, "access for past order denied"

