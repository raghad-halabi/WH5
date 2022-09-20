number = 76542
revers_number = 0
while number > 0:
    rev = number % 10
    revers_number = (revers_number * 10) + rev
    number = number // 10
print(revers_number)
