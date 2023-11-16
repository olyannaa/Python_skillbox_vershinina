def get_armstrong_numbers():
    for num in range(10, 100000):
        order = len(str(num))
        sum_of_digits = 0
        temp_num = num
        while temp_num > 0:
            digit = temp_num % 10
            sum_of_digits += digit ** order
            temp_num //= 10
        if num == sum_of_digits:
            yield num

for i in range(8):
    print(next(get_armstrong_numbers()), end=' ')
