import pytest
from black import nullcontext

from main import ClosedRange


class TestClosedRange:
    @pytest.fixture
    def closedrange(self):
        return ClosedRange(3, 8)

    def test_閉区間から下端点を取得できること(self, closedrange):
        assert closedrange.lower_endpoint == 3

    def test_閉区間から上端点を取得できること(self, closedrange):
        assert closedrange.upper_endpoint == 8

    def test_文字列表記(self, closedrange):
        assert str(closedrange) == "[3,8]"

    @pytest.mark.parametrize(
        ("lower_endpoint, upper_endpoint, expected"),
        [
            (3, 8, nullcontext()),
            (8, 8, pytest.raises(ValueError)),
            (8, 3, pytest.raises(ValueError)),
        ],
    )
    def test_下端点が上端点より必ず小さいこと(
        self, lower_endpoint, upper_endpoint, expected, closedrange
    ):
        with expected:
            ClosedRange(lower_endpoint, upper_endpoint)
