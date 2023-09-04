def test_a():
    assert ('home', 'work') == ('home', 'work')


def test_b():
    assert 'QA' != 'QC'

def test_c():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)