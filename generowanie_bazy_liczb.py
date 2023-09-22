def pritchard(max_num):
    wheel = [1]
    length = 1
    prime = 2
    primes = []

    while prime*prime <= max_num:
        if length < max_num:
            for num in wheel:
                new_num = num + length
                if new_num > prime*length or new_num > max_num:
                    break
                wheel.append(new_num)
            length = min(prime*length,max_num)
        
        for num in wheel:
            if num % prime == 0:
                wheel.remove(num)
        
        primes.append(prime)
        prime = wheel[1] if prime != 2 else 3
        print("I'm alive!")

    if length < max_num:
        for num in wheel:
            new_num = num + length
            if new_num > prime*length or new_num > max_num:
                break
            wheel.append(new_num)

    wheel.remove(1)
    primes += wheel

    return primes

def numsys(number, num_list):
    odd = number % 2
    if odd:
        number -= 1

    first_prime = 0
    first_index = 0
    second_prime = 0
    second_index = 0
    for i, num in enumerate(num_list):
        if num >= number:
            first_prime = num
            first_index = i
            break

    while first_prime + second_prime != number:
        first_index -= 1
        first_prime = num_list[first_index]
        while first_prime + second_prime < number:
            second_index += 1
            second_prime = num_list[second_index]

    def index_to_str(index):
        result = ""
        while index > 0:
            new_digit = (index-1)%6+1
            result += str(new_digit)
            index -= new_digit
            index //=6
        return result[::-1]
    #print(second_prime)
    #print(first_prime)
    slice_1 = index_to_str(second_index)
    slice_2 = "x" if odd else "o"
    slice_3 = index_to_str(first_index)[::-1]

    number_sys = slice_1 + slice_2 + slice_3

    return number_sys


import csv
import os
number_range=1000000
prime_list = pritchard(2*number_range)
prime_list.insert(0,1)
prime_list.insert(0,0)
with open("/kaggle/working/data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    print("Rozpoczeto zapisywanie!")
    for number in range(0,number_range):
        if number%1000==0:
            print(number)
        number_sys = numsys(number,prime_list)
        writer.writerow([number,number_sys])
file.close()

print('Plik został zapisany pomyślnie.')


#number = int(input())
#prime_list = pritchard(2*number)

# max_num = 10000
# prime_list = pritchard(2*max_num)
# prime_list.insert(0,1)
# prime_list.insert(0,0)
# for num in range(max_num):
#     print(numsys(num,prime_list))
