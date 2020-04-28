from unittest.mock import patch
from pytest_mock import mocker
from google_actions_helper import get_google_drive_files

# patching the api service not the actions helper function
@patch()
def test_get_google_drive_files(self, mock_get_google_drive_files):
    mock_get_google_drive_files.return_value = MagicMock(
        spec=Response, status_code=200, )
    get_google_drive_files('service')
    get_google_drive_files.assert_called_once_with('service')