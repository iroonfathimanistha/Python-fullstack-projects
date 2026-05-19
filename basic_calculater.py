def choose_operation(n1,n2,operation):
    if operation=='addition' or operation=='1':
        return n1+n2
    elif operation=='subtraction' or operation=='2'  :
        return n1-n2
    elif operation=='multiplication' or operation=='3':
        return n1*n2
    elif operation=='division' or operation=='4':
        return n1/n2

end_programe=False
while not end_programe:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number:"))
    operation = input(
        "\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n chooose the operation you need to use:").lower()
    result = choose_operation(num1, num2,operation)
    print(result)
    query = input("Doy you want to continue? (y/n):").lower()
    if query == 'n':
        end_programe =True
    else:
        end_programe =False



