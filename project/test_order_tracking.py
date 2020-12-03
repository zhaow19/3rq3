from project.account import Account
from project.order import Order


#The customer shall allow a customer to track the status of an order.
def test_order_tracking():
    if Account.acc_access == True & Order.order == True:
        assert Order.access_order_tracking == True, "The access for order tracking is granted."
    if Account.acc_access == True & Order.order == False:
        assert Order.access_order_tracking == False, "The access for order tracking is denied."
