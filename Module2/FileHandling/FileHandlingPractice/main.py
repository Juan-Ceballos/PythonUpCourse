import csv

with open('employee_data.csv', 'r') as csv_file:
    #with keyword file will be closed at end
    csv_reader = csv.DictReader(csv_file)
    # take in csv and return dictionary of file
    line_count = 0
    for row in csv_reader:
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

