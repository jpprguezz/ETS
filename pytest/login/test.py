import pytest

from login import RRSS

@pytest.fixture
def social_network():
    return RRSS()

def test_login(social_network: RRSS):
    social_network.create_account("juanito@hotmail.com", "elmasbonito123")
    assert social_network.login("juanito@hotmail.com", "elmasbonito123")

def test_failed_login(social_network: RRSS):
    social_network.create_account("marianita@yahoo.net", "1234abcd")
    assert not social_network.login("marianita@yahoo.net", "abcd1234")