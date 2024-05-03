def collect_inputs():
    pass

def get_currency_rates(file_path):
    pass

def convert_currency(amount, source_currency, target_currency, rates):
    if source_currency == target_currency:
        return amount
    try:
        result = amount * rates[source_currency][target_currency]
    except KeyError:
        raise ValueError('Given currency is not in rates')

    return result

def main():
    pass

if __name__ == '__main__':
    main()