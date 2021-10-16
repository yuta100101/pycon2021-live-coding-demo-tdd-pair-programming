import pytest
from black import nullcontext

from main import ClosedRange, OpenedRange


class TestClosedRange:
    @pytest.fixture
    def closedrange(self):
        return ClosedRange(3, 8)

    def test_value_of_lower_endpoint(self, closedrange):
        assert closedrange.lower_endpoint == 3

    def test_value_of_upper_endpoint(self, closedrange):
        assert closedrange.upper_endpoint == 8

    def test_str_format(self, closedrange):
        assert str(closedrange) == "[3,8]"

    @pytest.mark.parametrize(
        ("lower_endpoint, upper_endpoint, expected"),
        [
            (3, 8, nullcontext()),
            (8, 8, pytest.raises(ValueError)),
            (8, 3, pytest.raises(ValueError)),
        ],
    )
    def test_lower_endpoint_is_lower_than_upper_endpoint(
        self, lower_endpoint, upper_endpoint, expected
    ):
        with expected:
            ClosedRange(lower_endpoint, upper_endpoint)

    @pytest.mark.parametrize(("target, expect"), [(5, True), (-1, False)])
    def test_contains_integer(self, closedrange, target, expect):
        assert closedrange.contains(target) == expect

    @pytest.mark.parametrize(
        ("lower_endpoint, upper_endpoint, expected"),
        [
            (3, 8, True),
            (1, 6, False),
        ],
    )
    def test_eq_closed_range(
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
    def test_is_connected_to(
        self, lower_endpoint, upper_endpoint, expected, closedrange
    ):
        assert (
            closedrange.is_connected_to(ClosedRange(lower_endpoint, upper_endpoint))
        ) == expected


class TestOpenedRange:
    @pytest.fixture
    def openedrange(self):
        return OpenedRange(3, 8)

    def test_value_of_lower_endpoint(self, openedrange):
        assert openedrange.lower_endpoint == 3

    def test_value_of_upper_endpoint(self, openedrange):
        assert openedrange.upper_endpoint == 8

    def test_str_format(self, openedrange):
        assert str(openedrange) == "(3,8)"

    @pytest.mark.parametrize(
        ("lower_endpoint, upper_endpoint, expected"),
        [
            (3, 8, nullcontext()),
            (9, 8, pytest.raises(ValueError)),
            (8, 8, pytest.raises(ValueError)),
        ],
    )
    def test_lower_endpoint_is_lower_than_upper_endpoint(
        self, lower_endpoint, upper_endpoint, expected
    ):
        with expected:
            OpenedRange(lower_endpoint, upper_endpoint)
