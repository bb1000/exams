from solutions import (
    extract_emails,
    sendmail_format,
    Emp,
    read_list_of_employees,
    japan_sendlist,
)

def test_11a():
    assert extract_emails('tests/solutions/first.csv') == ['cdegregoli0@epa.gov']

def test_11b():
    assert extract_emails('staff.csv') == [
    'cdegregoli0@epa.gov',
     'astutt1@oracle.com',
     'eherkess2@google.com.au',
     'mdublin3@dion.ne.jp',
     'jreadwing4@craigslist.org',
     'bscattergood5@wiley.com',
     'aminkin6@purevolume.com',
     'abradburne7@quantcast.com',
     'ashoemark8@yahoo.co.jp',
     'igibbins9@geocities.com'
]

def test_12a():
    assert sendmail_format('first.csv') == 'cdegregoli0@epa.gov'

def test_12b():
    assert sendmail_format('staff.csv') == (
        'cdegregoli0@epa.gov;'
        ' astutt1@oracle.com;'
        ' eherkess2@google.com.au;'
        ' mdublin3@dion.ne.jp;'
        ' jreadwing4@craigslist.org;'
        ' bscattergood5@wiley.com;'
        ' aminkin6@purevolume.com;'
        ' abradburne7@quantcast.com;'
        ' ashoemark8@yahoo.co.jp;'
        ' igibbins9@geocities.com'
    )

employee = Emp('1,Conn,De Gregoli,cdegregoli0@epa.gov,"Kunze, Crona and Bergnaum"')
def test_21a():
    assert employee.first == 'Conn'

def test_21b():
    assert employee.last == 'De Gregoli'

def test_21c():
    assert employee.email == 'cdegregoli0@epa.gov'

def test_22():
    assert str(employee) == 'Conn De Gregoli <cdegregoli0@epa.gov>'

def test_31a():
    ## empty file
    with open('empty.csv', 'w'):
        pass
    assert read_list_of_employees('empty.csv') == []

def test_31b():
    assert read_list_of_employees('staff.csv')[0].first == 'Conn'
    assert read_list_of_employees('staff.csv')[1].first == 'Anette'

def test_32a():
    assert japan_sendlist('empty.csv') == ''

def test_32b():
    assert japan_sendlist('staff.csv') == (
        'Montgomery Dublin <mdublin3@dion.ne.jp>;'
        ' Abramo Shoemark <ashoemark8@yahoo.co.jp>'
    )

