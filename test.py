from app import capitalize


def test_capitalize_small_caps():
    assert capitalize('test') == 'Test'


def test_capitalize_all_caps():
    assert capitalize('TEST') == 'Test'


def test_mixed_caps():
    assert capitalize('tEsT') == 'Test'


def test_capitalize_two_words():
    assert capitalize('hello world') == 'Hello World'


def test_capitalize_hungarian():
    assert capitalize('áron') == 'Áron'
