def fizzBuzz(n):
    out = []
    for i in range(1, n + 1):
        handle_individual_number(i, out)
    for item in out: print(item)
    return out


def handle_individual_number(n, out):
    divisible_3 = n%3 == 0
    divisible_5 = n%5 == 0
    if all([divisible_3, divisible_5]): out.append('FizzBuzz')
    else:
        if divisible_3: out.append('Fizz')
        elif divisible_5: out.append('Buzz')
        else: out.append(n)
