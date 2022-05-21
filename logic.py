# some logic here
import math
b = 99999999999999


def who_is_gosha():
    '''returns who is gosha'''
    return 'daun'


def sum_of_numbers(n: int) -> int:
    '''returns the sum of numbers'''
    return sum(list(int(i) for i in str(n)))

    
def mult_of_numbers(n: int) -> int:
    '''returns the numbers multiplied'''
    a = 1
    for i in list(str(n)):
        a *= int(i)
    return a


def mult_of_numbers_remove_zero(n: int) -> int:
    '''returns all the numbers
except of zero multiplied'''
    a = 1
    for i in list(filter(lambda x: x != '0', list(str(n)))):
        a *= int(i)
    return a


def number_len(n: int) -> int:
    '''length function -- сделать склонения 
ala "шестизначное число"'''
    return len(str(n))


def number_divisor_list(n: int) -> list:
    '''returns list of divisors -- unoptimised'''
    divisors_list = list(filter(lambda x: n % x == 0, range(1, int(n**.5)+1))) + [n]
    return divisors_list


def biggest_divisor_of_2(n: int) -> int:
    '''returns the biggest divisor could be splitted by 2 -- unoptimised'''
    divisors_list = number_divisor_list(n)
    return max(list(filter(lambda x: x % 2 == 0, divisors_list)))


def number_of_divisors(n: int) -> int:
    '''returns number of divisors -- unoptimised'''
    divisors_number = len(list(filter(lambda x: n % x == 0, range(1, n))) + [n])
    return divisors_number


def is_prime(n: int) -> str:
    '''returns if number is prime'''
    if list(filter(lambda x: n % x == 0, range(2, n))):
        return False
    else:
        return True


def is_semiprime(n: int) -> str:
    '''returns if number is semiprime'''
    number_of_divisors = number_divisor_list(n)
    del number_of_divisors[0]
    del number_of_divisors[-1]
    print(number_of_divisors)
    if is_prime(n):
        return 'Нет'
    else:
        if all(map(is_prime, number_of_divisors)):
            return 'Да'
        else:
            return 'Нет'


def reversed_number(n: int) -> float:
    return n ** -1


def roman_equivalent(data: int) -> str:
    '''returns number in romans lang'''
    base = "I"*data
    
    base = base.replace("I"*5, "V")
    base = base.replace("V"*2, "X")
    base = base.replace("X"*5, "L")
    base = base.replace("L"*2, "C")
    base = base.replace("C"*5, "D")
    base = base.replace("D"*2, "M")
    
    base = base.replace("DCCCC", "CM")
    base = base.replace("CCCC", "CD")
    base = base.replace("LXXXX", "XC")
    base = base.replace("XXXX", "XL")
    base = base.replace("VIIII", "IX")
    base = base.replace("IIII", "IV")
    
    return base


def enToArNumb(number: int) -> str: 
    '''returns number in arabic'''
    dic = {
        '0': '۰',
        '1': '١',
        '2': '٢',
        '3': '۳',
        '4': '٤',
        '5': '۵',
        '6': '٦',
        '7': '۷',
        '8': '۸',
        '9': '۹',
    }
    ar_numbers = [dic.get(num) for num in str(number)]
    return ''.join(ar_numbers)


def morze():
    '''returns who i am'''
    return 'ya yeban'


def factorise(n: int) -> list:
    '''returns list of all the prime divisors -- fix "return" with multiple signs'''
    def prime_divisors(n):
        sieve = [True] * (n + 1)
    
        for x in range(2, int(len(sieve) ** 0.5) + 1):
            if sieve[x]: 
                for i in range(x + x, len(sieve), x):
                    sieve[i] = False
    
        lowerPrimes = [i for i in range(2, len(sieve)) if sieve[i] and (n % i == 0)]
        return lowerPrimes

    a = prime_divisors(n)
    lst = []

    while n != 1:
        b = list(filter(lambda x: n % x == 0, a))[0]
        lst.append(b)
        n //= b    
    return lst


def binary_representation(n: int) -> int:
    '''returns binary representation of number'''
    return str(bin(n))[2:]
        

def ternary (n: int) -> int:
    '''returns число в троичной системе счисления'''
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums)) 