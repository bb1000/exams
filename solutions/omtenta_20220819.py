import collections

### BEGIN SOLUTION
def minmax(sequence, default=None, key=None):
    if len(sequence) == 0:
        return (default, default)
    return min(sequence, key=key), max(sequence, key=key)
### END SOLUTION

def minmax_keys(dct):
    ### BEGIN SOLUTION
    return minmax(dct)
    ### END SOLUTION

def minmax_values(dct):
    ### BEGIN SOLUTION
    return minmax(dct.values())
    ### END SOLUTION

def keys_of_minmax_values(dct):
    ### BEGIN SOLUTION
    return minmax(dct, key=lambda x: dct[x])
    ### END SOLUTION

def minmax_items(dct):
    ### BEGIN SOLUTION
    return minmax(dct.items())
    ### END SOLUTION
### BEGIN SOLUTION
MinMax = collections.namedtuple('MinMax', ['min', 'max'])
def minmax2(*args, default=None, key=None):
    if len(args) == 1:
        sequence = args[0]
    else:
        sequence = args
    mm = minmax(sequence, default=default, key=key)
    return MinMax(*mm)
### END SOLUTION
