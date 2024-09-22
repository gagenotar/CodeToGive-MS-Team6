from ..services.word_spinner import WordSpinner

def test_spin():
    text = "This is a test."
    spun_text = WordSpinner.spin(text)
    assert spun_text == text  # no actual spinning logic is implemented yet
