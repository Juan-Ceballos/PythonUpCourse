import csv
from itertools import count

with open('employee_data.csv', 'r') as csv_file:
    #with keyword file will be closed at end
    csv_reader = csv.DictReader(csv_file)
    # take in csv and return dictionary of file
    line_count = 0
    for row in csv_file:
        if line_count == 0:
            line_count += 1
        print(row)
        line_count += 1
        print(f'Processed {line_count} lines.')

# Code if was opening csv file and reading using import csv to take file and turn to dictionary that can manipulate to
# take and print info in file

#file = open('myfile.txt', 'r')
#contents = file.read()
#print(contents)
#file.close()

# Part 2
# a instead of r to append add to end of file
# w for write will overwrite existing content
# w new file and .write to write

with open('myfile.txt', 'a') as file:
    file.write('\nThis is some new text which was appended')

# last one added this one overrides
# with open('myfile.txt', 'w') as file:
#     file.write('\nThis is some new text which was appended')
#     file.colse()

fruit_list = ["Apple", "Orange", "Grapes"]
with open('myfile.txt', 'w') as my_file:
    for fruit in fruit_list:
        my_file.write("\n" + fruit)

content = open('myfile.txt') # file already exist but can open new using open
print(content.read())


# can iterate and write

with open('myfile.txt', 'w') as file2:
    file2.write("Hello overwriting to count words")

def count_words(file_path):
    with open(file_path) as file:
        data = file.read()
        data.replace(",", " ")
        return len(data.split(" "))

print(count_words('myfile.txt'))

