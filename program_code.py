# Write a Python program that reads a text file named numbers.txt that contains 20 numbers. The program will create
# two other text file; the first text file will be named even.txt that will contains all even numbers extracted from
# the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the
# numbers.txt.

# open numbers.txt (read), even.txt (append), odd.txt (append)
with open('numbers.txt') as integers, open('even.txt', 'a') as even_int, open('odd.txt', 'a') as odd_int:
    # read numbers.txt line by line
    for line in integers:
        print('a')
        # if even, write to even.txt
        # if odd, write to odd.txt
