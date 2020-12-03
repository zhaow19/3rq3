from project.status_check import Check
from project.order import Order

#The system shall allow customer to check the status of the order
def test_order_status():
    statuscheck = True
    assert Check.status_check == Order.status, "The status should presents."