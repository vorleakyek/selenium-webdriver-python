import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def data_load():
    print("data is being created")
    return ['first', 'last', 'email']


@pytest.fixture(params=[("chrome", "first", "last"), ("Firefox", "last"), ("IE", "name")])
def cross_browser(request):
    return request.param
