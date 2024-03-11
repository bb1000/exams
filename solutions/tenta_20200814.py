def extract_emails(filename):
    ### BEGIN SOLUTION
    with open(filename)as f:
        return [line.split(',')[3] for line in f]
    ### END SOLUTION
