import csv

# Prompt for the filename
filename = input("Please enter the filename: ")

# Display the contents of the file
with open(filename, mode='r', encoding='UTF-16') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    # Remove '/2022' from the header row
    header_row = next(csv_reader)
    print(header_row)

    for i in header_row:
        if i.find("/2022") != -1:
            print(str(i) + " contains '/2022'!")
            i = i.replace('/2022', '')
            print('After replace: ' + str(i))

    #for row in csv_reader:
        #print(row)