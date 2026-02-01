from app.hangman import reveal_word, is_word_guessed


def test_reveal_word_single_letter():
    assert reveal_word("python", {"p"}) == "p _ _ _ _ _"


def test_is_word_guessed_true():
    assert is_word_guessed("hi", {"h", "i"}) is True


def test_is_word_guessed_false():
    assert is_word_guessed("hi", {"h"}) is False
