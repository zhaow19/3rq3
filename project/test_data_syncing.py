from project.web_data import Web
from project.mobile_data import Mobile

#The system shall allow data are synced between DIS website and the DIS mobile application.
def test_data_sync():
    webdata = Web.web_data
    mobdata = Mobile.mobile_data
    assert webdata == mobdata, "The data between website and mobile app are synced."

