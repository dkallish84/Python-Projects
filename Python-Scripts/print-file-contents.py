import csv

storage_list = []

# Prompt for the filename
filename = input("Please enter the filename: ")

# Display the contents of the file
with open(filename, mode='r', encoding='UTF-16') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for row in csv_reader:
        # Store each row as a list to be processed
        storage_list = row
        # Check the range & length of the storage list
        for i in range(len(storage_list)):
            # If the value contains '/2022' remove it to be 'm/d' notation
            if str(storage_list[i]).find('/2022') != -1:
                print(str(i) + " contains '/2022'")
                storage_list[i] = str(storage_list[i]).replace('/2022', '')

        print(storage_list)