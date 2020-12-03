from project.order import Order

#The system shall allow a customer to check the current location of an order when the order is out of delivery
def test_delivery_location_check():
    if Order.access_order_tracking == True:
        assert Order.order_location == "*******(current location)", "The current location of the order should present"
    if Order.access_order_tracking == False:
        assert Order.order_location == False, "The current location is unavaliable"
