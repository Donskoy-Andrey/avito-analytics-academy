import pytest
from morse import decode


@pytest.mark.parametrize("morse, expected", [
    ('.... . .-.. .-.. ---', 'HELLO'),
    ('--. --- --- -..', 'GOOD'),
    ('... --- ...', 'SOS')
])
def test_decode(morse, expected):
    assert decode(morse) == expected
