# pt 1
def captcha():
    number = input('Enter the puzzle input')
    digits = number + number[0]
    return sum([int(digit) for index, digit in enumerate(number)
                if digit == digits[index+1]])


# pt 2
def captcha2():
    numbers = input('Enter input here:')
    halfway = int(len(numbers) / 2)
    digits = numbers + numbers[:halfway]
    return sum([int(digit) for index, digit in enumerate(numbers)
                if digit == digits[index+halfway]])
