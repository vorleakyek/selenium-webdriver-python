import pytest


@pytest.mark.usefixtures("data_load")
class TestExample2:

    def test_edit_username(self, data_load):
        print(data_load)

