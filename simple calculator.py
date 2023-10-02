def simple_calc():
    #getting the numbers from the user
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    print(num1)
    print(num2)
    #calculating the sum, difference, multiplication and division
    sum=num1+num2
    difference=num1-num2
    product=num1*num2
    quotient=num1/num2
    #printing out the output
    print(f"sum: {sum}")
    print(f"difference: {difference}")
    print(f"product: {product}")
    print(f"quotient: {quotient}")

simple_calc()