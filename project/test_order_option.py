from project.order import Order

#The system shall allow customers to have a choice for the order that it is for delivery or take out.
def test_delivery_order():
    order = Order()
    #ask for input
    option = input("delivery or takeout")
    order.orderoption(options=option)
    if option == "delivery":
        assert order.orderoption(options="delivery"), "order option set to delivery"
    if option == "takeout":
        assert order.orderoption(options="take out"), "order option set to takeout"
