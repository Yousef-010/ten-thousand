import pytest
from tests.flo import diff
from ten_thousand.game import Game

# pytestmark = [pytest.mark.version_2]


def test_quitter():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/quitter.sim")
    assert not diffs, diffs


def test_one_and_done():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/one_and_done.sim")
    assert not diffs, diffs


def test_single_bank():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/bank_one_roll_then_quit.sim")
    assert not diffs, diffs


def test_bank_first_for_two_rounds():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/bank_first_for_two_rounds.sim")
    assert not diffs, diffs

# hot dice is stretch goal
# def test_hot_dice():
#     """When all dice are used without a zilch
#     then user gets 6 fresh dice and continues turn.
#     """
#     game = Game()
#     diffs = diff(game.play, path="hot_dice.sim")
#     assert not diffs, diffs


def test_repeat_roller():
    """Allow setting aside scoring dice and rolling the rest
    """
    game = Game()
    diffs = diff(game.play, path="tests/version_2/repeat_roller.sim")
    assert not diffs, diffs

