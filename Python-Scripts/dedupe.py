# Import the CSV class
import csv

# Prompt for the filename
filename = input("Enter the filename: ")

# Assumes first column is 'First Dimension' and third column is ''(Cases)
cols_to_remove = [0, 2]
cols_to_remove = sorted(cols_to_remove, reverse=True)
row_count = 0
# Store the rows that have been seen in a list
row_seen = []
# Store the cleaned data
cleaned = []

# Open the specified file, assumes UTF-16 and tab delimited
with open(filename, mode='r', encoding='UTF-16') as input_file:
    reader = csv.reader(input_file, delimiter='\t')

    # Create an output file with the cleaned data
    with open('Cleaned_'+filename, mode='w', newline='') as output_file:
        writer = csv.writer(output_file)

        for row in reader:
            for col_index in cols_to_remove:
                # Remove the specified columns from each row (dictionary)
                del row[col_index]
                # Update the cleaned list
                cleaned.append(row)

        for row in cleaned:
            # Relabel the 'View By' column to blank
            if str(row[0]) == "View By":
                row[0] = ''
            # Check if the 'View By' column has been seen so it's not duplicated in the file
            elif row[0] in row_seen:
                continue
            else:
                # Add the 'View By' value to the row_seen list
                row_seen.append(row[0])
                # Write the result to the file
                writer.writerow(row)
                
    print("File processed and saved as Cleaned_" + filename)
    