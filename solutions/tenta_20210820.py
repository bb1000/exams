import pandas

def get_usd(date_string, filename):
    """
    Returns exchange rate in file for given date
    """
    ### BEGIN SOLUTION
    with open(filename) as f:
        for line in f:
            date, value = line.split(',')
            if date[:10] == date_string:
                break
    return float(value)
    ### END SOLUTION

def get_usd_as_dict(filename):
    """
    Returns a dictionary with dates as keys and exchange rate as values
    """
    ### BEGIN SOLUTION
    d = {}
    with open(filename) as f:
        for line in f:
            date, value = line.split(',')
            d[date[:10]] = float(value)
    return d
    ### END SOLUTION

def get_index_max_value(dct):
    ### BEGIN SOLUTION
    return sorted(dct, key=lambda k: dct[k])[-1]
    ### END SOLUTION

def dca(dct):
    """
    Return total btc acuumulated from $1/day
    """
    ### BEGIN SOLUTION ###
    btc = 0
    daily = 1.0
    for v in dct.values():
        btc += daily/v
    return btc
    ### END SOLUTION

_data = (
    pandas.read_csv('market-price.csv'),
    pandas.read_csv('market-price.csv', names=['date', 'USD']),
    pandas.read_csv('market-price.csv', names=['date', 'USD']).set_index('date'),
    pandas.read_csv('market-price.csv', names=['date', 'USD'], parse_dates=[0]).set_index('date')['USD']
)
data0, data1, data2, data3 = _data

### BEGIN SOLUTION
exchange_rates0 = pandas.read_csv('exchange-rates.csv', parse_dates=[0])
### END SOLUTION

### BEGIN SOLUTION
exchange_rates1 = pandas.read_csv('exchange-rates.csv', parse_dates=[0])
isodate = exchange_rates1.Date.apply(lambda x: x.isoformat()[:10])
exchange_rates1['isodate'] = isodate
### END SOLUTION

### BEGIN SOLUTION
exchange_rates2 = pandas.read_csv('exchange-rates.csv', parse_dates=[0])
isodate = exchange_rates2.Date.apply(lambda x: x.isoformat()[:10])
exchange_rates2['isodate'] = isodate
exchange_rates2.set_index('isodate', inplace=True)
us2sek = exchange_rates2['SEK']
### END SOLUTION

def convert(f):
    ### BEGIN SOLUTION
    def wrap(*args, **kwargs):
        result = f(*args, **kwargs)
        return us2sek[args[0]] * result
    return wrap
    ### END SOLUTION


get_sek = convert(get_usd)

