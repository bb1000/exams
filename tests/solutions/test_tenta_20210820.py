import pandas

from solutions.tenta_20210820 import (
    get_usd,
    get_usd_as_dict,
    get_index_max_value,
    dca, _data,
    exchange_rates0,
    #exchange_rates1,
    #exchange_rates2,
    us2sek,
    get_sek,
)

def test_11():
    result = get_usd('2021-04-01', 'market-price.csv')
    expected = 58735.25
    assert result == expected, f'{result} != {expected}'

    assert get_usd('2021-08-19', 'market-price.csv') == 44777.86

def test_12():
    usd = get_usd_as_dict('market-price.csv')
    assert usd['2021-04-01'] == 58735.25

def test_21():
    usd = get_usd_as_dict('market-price.csv')
    assert get_index_max_value(usd) == '2021-04-14'
    assert usd['2021-04-14'] == 63554.44

def test_22():
    usd = get_usd_as_dict('market-price.csv')
    assert dca({'2008-01-01': 10}) == .1
    assert dca({'2008-01-01': 10, '2008-01-02': 40}) == .125
    assert round(dca(usd), 8) == 0.01529260  # values is a dict from assignment 2

def test_25():
    assert isinstance(_data[0], pandas.DataFrame)

def test_26():
    assert all(_data[1].columns == ['date', 'USD'])

def test_27():
    assert _data[2].columns == ['USD']
    assert _data[2].index.name == 'date'

def test_28():
    assert isinstance(_data[3], pandas.Series)
    assert _data[3].name == 'USD'
    assert _data[3].index.name == 'date'
    assert _data[3].dtype == 'float'

def test_39():
    assert isinstance(exchange_rates0.iloc[0]['Date'], pandas.Timestamp)

def test_310():
    assert isinstance(us2sek, pandas.Series)
    assert us2sek['2020-08-18'] == 8.6679

def test_311():
    assert get_sek('2020-08-20', 'market-price.csv').round(2) == 102541.08
    assert get_sek('2021-08-18', 'market-price.csv').round(2) == 389366.78
