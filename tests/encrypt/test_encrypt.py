import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1989, 5)
        encrypt_message('Nícolas', 'bla')
    assert encrypt_message('comida', 10) == 'adimoc'
    assert encrypt_message('alimento', 4) == 'otne_mila'
