# list all of the numbers that multiples of 3 and 5 below 1000
def sum_of_multiples_of_3_and_5():
    multiples_list = [x for x in range(1, 1000) if (x % 3 == 0) or (x % 5 == 0)]
    print(multiples_list)
    return sum(multiples_list)
        
#print(sum_of_multiples_of_3_and_5())
#sum_of_multiples_of_3_and_5()

def even_fibonacci_numbers():
    fib_list = [0, 1] # given elements

    for n in range(2, 100):
        next_element = fib_list[n-1] + fib_list[n-2]
        fib_list.append(next_element)

    temp_list = [ fib_list[j] 
        for j in range(0, len(fib_list)) 
        if fib_list[j] < 4000000 and fib_list[j] % 2 == 0
    ] 
    return sum(temp_list)

def fibonacci():
    fib_list = [0, 1]
    for n in range(len(fib_list),100):
        next_element = fib_list[n-1] + fib_list[n-2]
        fib_list.append(next_element)
    return fib_list

def golden_ratio(arr):
    for n in range(2, len(arr) - 1):
        b = arr[n+1]
        a = arr[n]
        calculate_golden_ratio = b / a
        print('{} / {} = {}'.format(b, a, calculate_golden_ratio))
# 5


def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n-1) * n

# print(even_fibonacci_numbers())

print(golden_ratio(fibonacci()))