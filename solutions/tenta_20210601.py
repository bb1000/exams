import requests

def get_usernames(source: str) -> list:
    """
    Returns username from a file of mail addresses as a list
    """
    ### BEGIN SOLUTION
    with open(source) as f:
        users = []
        for line in f:
            users.append(line.split('@')[0])
    return users
    ### END SOLUTION

def _get_usernames_by_affiliation(source: str) -> list:
    """
    Returns usernames from a file grouped by affiliation
    """
    ### BEGIN SOLUTION
    users = {}
    with open(source) as f:
        for line in f:
            user, url = line.split('@')
            aff, _ = url.split('.')
            if aff not in users:
                users[aff] = []
            users[aff].append(user)
    return users
    ### END SOLUTION

def get_usernames_by_affiliation(source: str) -> dict:
    """
    Returns usernames from a file as a dictionary grouped by affiliation
    """
    users = {}
    with open(source) as f:
        for line in f:
            username, domain = line.split('@')
            affiliation, _ = domain.split('.')
            if affiliation not in users:
                users[affiliation] = []
            users[affiliation].append(username)
    return users

### BEGIN SOLUTION
class Employee:
    all = []
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
        Employee.all.append(self)

    def __str__(self):
        return f'{self.first} {self.last} <{self.email}>'

    def __repr__(self):
        return f'Employee("{self.first}", "{self.last}", "{self.email}")'

    @staticmethod
    def to_mail_file(filename):
        with open(filename, 'w') as f:
            for e in Employee.all:
                print(e.email, file=f)

### END SOLUTION

def ChalmersHack(cls):
    ### BEGIN SOLUTION
    def wrapper(*args, **kwargs):
        emp = cls(*args, **kwargs)
        emp.email = emp.email.split('@')[0] + '@chalmers.se'
        return emp
    return wrapper
    ### END SOLUTION

def get_users(users):
    ### BEGIN SOLUTION
    url = 'https://api.kth.se/api/profile/1.1/'
    for u in users:
        r = requests.get(url + u).json()
        yield Employee(r['givenName'], r['familyName'], r['email']), r['image']
    ### END SOLUTION
