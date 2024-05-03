import json


def main():
    amount = float(input('Enter amount: '))
    source = input('Enter source currency: ')
    target = input('Enter target currency: ')
    rates = json.load(open('./rates.json'))
    result = amount * rates[source][target]
    print(f'{amount} {source} = {result} {target}')

if __name__ == '__main__':
    main()