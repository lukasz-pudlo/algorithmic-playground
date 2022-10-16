import time

st = time.process_time()


def exponentialise(number, exponent):
    print('When number is', number, 'and exponent is', exponent,
          'we can perform a simple calculation using number ** exponent', number ** exponent)
    if exponent == 1:
        return number
    else:
        return exponentialise(number, exponent - 1) * number


print(exponentialise(2, 7))

et = time.process_time()

res = et - st
milliseconds_result = res * 1000

print('Result in milliseconds is', milliseconds_result, 'milliseconds')
