import pytest


@pytest.fixture()
def setup():
    print("this is fixture setup")
    yield
    print("this is yield last line")

def test_fixturedemo(setup):
    print("this is demo")