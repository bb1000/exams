import tempfile

from solutions import (
    get_usernames,
    get_usernames_by_affiliation,
    Employee,
    ChalmersHack,
    get_users,
)

def test_11a():
    users = get_usernames("emails.txt")
    expected = ["bonnie", "clyde", "scarlett", "rhett"]
    assert users == expected, f'\n{users} \n!= \n{expected}'

def test_11b():
    with tempfile.NamedTemporaryFile('w') as t:
        print('foo@bar.se\nbaz@boo.uk', file=t, flush=True)
        users = get_usernames(t.name)

    expected = ['foo','baz']
    assert users == expected, f'{users} != {expected}'

def test_12():
    users = get_usernames_by_affiliation('emails.txt')
    expected = {'kth': ['bonnie', 'scarlett'], 'chalmers': ['clyde', 'rhett']}
    assert users == expected, f'\n{users} \n!= \n{expected}'


def test_21():
    record = {
        'givenName': 'Sigbritt',
        'familyName': 'Karlsson',
        'url': 'https://www.kth.se/profile/sigbritt',
        'email': 'rektor@kth.se',
    }

    args = (record['givenName'], record['familyName'], record['email'])
    rector = Employee(*args)
    assert rector.first == 'Sigbritt'
    assert rector.last == 'Karlsson'
    assert rector.email == 'rektor@kth.se'

def test_22():
    _Employee = ChalmersHack(Employee)
    emp = _Employee('John', 'Doe', 'jd@kth.se')
    assert emp.email == 'jd@chalmers.se'

def test_31():
    users = get_users(['soderhol', 'mil'])
    result = next(users)
    expected = Employee('Anders', 'Söderholm', 'rektor@kth.se'),\
        'https://www.kth.se/files/avatar/soderhol'

    assert result[1] == expected[1], f'\n{result[1]} \n!=\n{expected[1]}'
