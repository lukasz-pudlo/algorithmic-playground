import time

st = time.process_time()


def exponentialise(number, exponent):
    if exponent == 1:
        return number
    elif number % 2 == 0:
        result = exponentialise(number, exponent // 2)
        return result * result
    elif number % 2 == 1:
        result == exponentialise(number, exponent // 2)
        return result * result * number


print(exponentialise(1000, 100000))

et = time.process_time()

res = et - st
milliseconds_result = res * 1000

print('Result in milliseconds is', milliseconds_result, 'milliseconds')
