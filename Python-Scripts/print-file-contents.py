import csv

# Prompt for the filename
filename = input("Please enter the filename: ")

# Display the contents of the file
with open(filename, mode='r', encoding='UTF-16') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for row in csv_reader:
        # Check the range & length of the storage list
        for i in range(len(row)):
            # If the value contains '/2022' remove it to be 'm/d' notation
            if str(row[i]).find('/2022') != -1:
                row[i] = str(row[i]).replace('/2022', '')

        print(row)