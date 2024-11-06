import pytest
from PageObject.Video import Automation_video


@pytest.mark.usefixtures('driver')
class Test_Automated_video:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.log_in = Automation_video(self.driver)

    # Test cases to run the test
    @pytest.mark.Autoamated_video  # used marker functionality
    def test_01(self):
        self.log_in.Video()
