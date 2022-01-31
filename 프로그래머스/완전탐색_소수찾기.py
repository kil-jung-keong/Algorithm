from itertools import *
def make_all_case(numbers):
    all_case = []
    for i in range(1,len(numbers)+1):
        num_list = list(permutations(numbers,i))
        all_case.extend(num_list)
    all_case = set(all_case)
    all_case = list(all_case)
    return all_case

def merge(all_case):
    change_to_num = []
    for i in range(len(all_case)):
        change_to_num.append(''.join(all_case[i]))    
    return change_to_num


def to_num(num_list):
    result = []
    for str_num in num_list:
        int_num = int(str_num)
        result.append(int_num)
    result = list(set(result))
    return result

def find_prime_num(convert_to_num):
    result = convert_to_num.copy()
    for num in convert_to_num:
        if num == 0:
            result.remove(num)
        if num == 1:
            result.remove(num)
        else:
            for i in range(2,num):
                if num % i != 0:
                    continue
                else:
                    result.remove(num)
                    break
    return result

def solution(numbers):
    numbers = list(numbers)
    all_case = make_all_case(numbers)
    num_list = merge(all_case)
    convert_to_num = to_num(num_list)
    result = len(find_prime_num(convert_to_num))
    return result

print(solution("011"))