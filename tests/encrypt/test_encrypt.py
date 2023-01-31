from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('message', 5) == 'assem_eg'
    assert encrypt_message('message', 7) == 'egassem'
    assert encrypt_message('message', 2) == 'egass_em'

    with pytest.raises(TypeError):
        encrypt_message(4, 5)
    with pytest.raises(TypeError):
        encrypt_message("message", "1")
