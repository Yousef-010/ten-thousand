import pytest
from tests.flo import diff
from ten_thousand.game import Game

pytestmark = [pytest.mark.version_2]


def test_quitter():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/quitter.sim.txt")
    assert not diffs, diffs


def test_one_and_done():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/one_and_done.sim.txt")
    assert not diffs, diffs


def test_single_bank():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/bank_one_roll_then_quit.sim.txt")
    assert not diffs, diffs


def test_bank_first_for_two_rounds():
    game = Game()
    diffs = diff(game.play, path="tests/version_2/bank_first_for_two_rounds.sim.txt")
    assert not diffs, diffs


def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
    diffs = diff(Game().play, path="tests/version_3/hot_dice.sim.txt")
    assert not diffs, diffs


def test_repeat_roller():
    """Allow setting aside scoring dice and rolling the rest
    """
    diffs = diff(Game().play, path="tests/version_3/repeat_roller.sim.txt")
    assert not diffs, diffs