'''Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user'''
principal=int(input("Enter the Principal"))
time=int(input("Enter the Time"))
rate=int(input("Enter the Rate"))
SI=(principal*time*rate)/100
print("The simple Interest is:",SI)