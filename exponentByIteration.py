import time

st = time.process_time()


def exponentialise(number, exponent):
    result = number
    for i in range(1, exponent):
        result *= number
        i += 1
    return result


time.sleep(3)
print(exponentialise(3, 10000))

et = time.process_time()
final_result = et * 1000

elapsed_time = et - st
print('Execution time:', final_result, 'milliseconds')
