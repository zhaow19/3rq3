from project.account import AccountInfo

#The system shall automatically calculate the delivery fee and the estimated delivery time for a customer.
def calculated_delivery_fee_time():
    accountinfo =AccountInfo()
    calculated_fee =accountinfo.Account_info("1280 Main Street West, Hamilton, Ontario L8S 4L8")
    calculated_time = accountinfo.Account_info("1280 Main Street West, Hamilton, Ontario L8S 4L8")

    assert calculated_fee == 3, "delivery fee should be 3 dollars"
    assert calculated_time == 40, "delivery time should be 40 minutes"
