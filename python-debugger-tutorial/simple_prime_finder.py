from sys import argv

def find_primes(num):

    for potential_prime in range(2, num):
        if is_prime(potential_prime):
            print(potential_prime)


def is_prime(num):

    for index in range(2, num):
        if num % index == 0:
            return False
    
    return True


def main():

    input_num = int(argv[1])

    find_primes(input_num)


if __name__ == "__main__":
    main()
