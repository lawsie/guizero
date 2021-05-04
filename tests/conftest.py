import pytest
from time import sleep

@pytest.fixture(autouse=True)
def delay():
    # put a small delay in before every test,
    #  otherwise tkinter can get upset by the constant
    #  creating and destroying of apps
    sleep(0.1)