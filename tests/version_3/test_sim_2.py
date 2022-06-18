import pytest
from tests.flo import diff
from ten_thousand.game import Game

# pytestmark = [pytest.mark.version_3]


def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.Therefor the user's input must be validated If invalid prompt user for re-entry
    """
    diffs = diff(Game().play, path="tests/version_3/cheat_and_fix.sim")
    assert not diffs, diffs


def test_zilcher():
    """
    No scoring dice results in a 'zilch' which wipes away shelved points and ends turn
    """
    diffs = diff(Game().play, path="tests/version_3/zilcher.sim")
    assert not diffs, diffs