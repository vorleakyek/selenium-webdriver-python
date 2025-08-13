import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixture_demo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixture_demo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixture_demo3(self):
        print("I will execute steps in fixtureDemo3 method")

