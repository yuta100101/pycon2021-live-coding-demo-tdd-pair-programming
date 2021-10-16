import pytest
from black import nullcontext

from main import ClosedRange, OpenedRange


class TestRange:
    @pytest.fixture
    def closedrange(self):
        return ClosedRange(3, 8)

    @pytest.fixture
    def openedrange(self):
        return OpenedRange(3, 8)

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
    def test_下端点が上端点より必ず小さいこと(self, lower_endpoint, upper_endpoint, expected):
        with expected:
            ClosedRange(lower_endpoint, upper_endpoint)

    @pytest.mark.parametrize(("target, expect"), [(5, True), (-1, False)])
    def test_閉区間が任意の整数を含むか(self, closedrange, target, expect):
        assert closedrange.contains(target) == expect

    @pytest.mark.parametrize(
        ("lower_endpoint, upper_endpoint, expected"),
        [
            (3, 8, True),
            (1, 6, False),
        ],
    )
    def test_任意の下端点と上端点が等しい閉区間は等しいか(
        self, lower_endpoint, upper_endpoint, expected, closedrange
    ):
        assert (closedrange == ClosedRange(lower_endpoint, upper_endpoint)) == expected

    @pytest.mark.parametrize(
        ("lower_endpoint, upper_endpoint, expected"),
        [
            (1, 6, True),
            (8, 15, True),
            (9, 12, False),
        ],
    )
    def test_任意の2つの閉区間が接続しているか(
        self, lower_endpoint, upper_endpoint, expected, closedrange
    ):
        assert (
            closedrange.is_connected_to(ClosedRange(lower_endpoint, upper_endpoint))
        ) == expected
