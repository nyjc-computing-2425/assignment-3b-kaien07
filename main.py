stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
index = stdform.find('x')
power = stdform[index:].strip('x10^')
num = stdform[:index]
print(f'This number in E notation is {num}E{power}.')