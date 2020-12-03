from project.order import Order


#The system shall allow customers to choose how their orders can be delivered.
def validorder():
    pass

def test_delivery_options():
    Order.order == validorder
    assert Order.order_options == "Leave at door or Meet at door or Meet outside", "The delivery options should presented to the customer."