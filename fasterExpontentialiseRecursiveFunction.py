import time

st = time.process_time()


def exponentialise(number, exponent):
    if exponent == 1:
        return number
    elif exponent % 2 == 0:
        result = exponentialise(number, exponent // 2)
        return result * result
    elif exponent % 2 == 1:
        result = exponentialise(number, exponent // 2)
        return result * result * number


time.sleep(3)
print(exponentialise(3, 10000))

et = time.process_time()

final_result = et * 1000

elapsed_time = et - st
print('Execution time:', final_result, 'milliseconds')
