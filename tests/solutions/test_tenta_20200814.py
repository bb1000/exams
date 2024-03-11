from solutions import extract_emails

def test_1a():
    assert extract_emails('tests/solutions/first.csv') == ['cdegregoli0@epa.gov']
