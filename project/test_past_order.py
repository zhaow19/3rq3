from project.account import OrderHistory, Account
from project.order import Order
#The system shall allow customers to check their past orders after login.

def test_order_history():

    if Account.acc_access ==  True:
        assert OrderHistory.Access_Past_Order == True, "access for past order granted"
    if Account.acc_access == False:
        assert OrderHistory.Access_Past_Order == False, "access for past order denied"


#The system shall provide an option for customers to reorder their past orders.

def reorderpastorder():
    pass

def test_reorder_past_order():
    reorderpastorder == True
    assert Order.order == OrderHistory.Past_Order, "reorder successfully, past order item should presented in shopping cart."