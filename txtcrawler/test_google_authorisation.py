import mock
from pytest_mock import mocker
from google_authorisation import Auth

@mock.patch('google_authorisation.Auth')
# todo assert called with, rather than making it return a value
def test_auth_inst(mock_class):
    mock_class.return_value.start_service_object.return_value =
