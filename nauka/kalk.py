num1 = float(input('wpisz pierwszy numer'))
num2 = float(input('wpisz drugi numer'))

operation = input('wybierz_operacje: \n'
    '1. Addition\n'
    '2. substraction\n'
    '3. multiplication\n'
    '4. division\n')

if operation == '1':
    print('Result: ', num1 + num2)
elif operation == '2':
    print('Result: ', num1 - num2)
elif operation == '3':
    print('Result: ',num1 * num2)
elif operation == '4':
    print('Result: ', num1 / num2)
                
                
                