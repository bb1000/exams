def extract_emails(filename):
    ### BEGIN SOLUTION
    with open(filename)as f:
        return [line.split(',')[3] for line in f]
    ### END SOLUTION

def sendmail_format(filename):
    ### BEGIN SOLUTION
    emails = extract_emails(filename)
    return "; ".join(emails)
    ### END SOLUTION

class Employee:
    ### BEGIN SOLUTION
    def __init__(self, line):
        self.first, self.last, self.email = line.split(',')[1:4]

    def __str__(self):
        return f'{self.first} {self.last} <{self.email}>'
    ### END SOLUTION

def read_list_of_employees(filename):
    ### BEGIN SOLUTION
    return list(map(Employee, open(filename)))
    ### END SOLUTION

def japan_sendlist(filename):
    employees = read_list_of_employees(filename)
    ### BEGIN SOLUTION
    def is_jap(employee):
        return employee.email.endswith('.jp')
    filtered = filter(is_jap, employees)
    return '; '.join(map(str, filtered))
    ### END SOLUTION
