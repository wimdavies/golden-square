from lib.time_error import TimeError
from unittest.mock import Mock

def test_returns_difference_between_remote_and_local_time():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime": 1714559035}
    timer_mock = Mock()
    timer_mock.time.return_value = 1714559035.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -0.5
