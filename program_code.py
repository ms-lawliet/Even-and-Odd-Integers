# Write a Python program that reads a text file named numbers.txt that contains 20 numbers. The program will create
# two other text file; the first text file will be named even.txt that will contains all even numbers extracted from
# the numbers.txt. The second text file will be named odd.txt that will contains all odd numbers extracted from the
# numbers.txt.

class Integers:
    def __init__(self, file):
        self.file = file

    def extract(self):
        # open numbers.txt (read), even.txt (append), odd.txt (append)
        with open(self.file) as integers, open('even.txt', 'a') as even_int, open('odd.txt', 'a') as odd_int:
            # read numbers.txt line by line
            for line in integers:
                num = int(line)
                # if even, write to even.txt
                if num % 2 == 0:
                    even_int.write(f'{str(num)}\n')
                # if odd, write to odd.txt
                else:
                    odd_int.write(f'{str(num)}\n')


to_extract = Integers('numbers.txt')
to_extract.extract()
