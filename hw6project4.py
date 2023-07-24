sum = 0
n = 1
count = float(input("Enter the number of numbers to be averaged: "))

while n <= count:
  number = float(input("Enter a number: "))
  sum += number
  n += 1

avg = sum / count
print(f"The sum is: {sum}")
print(f"The average is: {avg}")