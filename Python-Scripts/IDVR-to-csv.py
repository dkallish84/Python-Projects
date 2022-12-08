# Import the CSV class
import csv, sys

# Check to see if a file was passed as an argument
try:
    filename = sys.argv[1]
except:
    # If no argument was passed, prompt for the filename
    filename = input("Enter the filename: ")

# Assumes first column is 'First Dimension' and third column is ''(Cases)
cols_to_remove = [0, 2]
cols_to_remove = sorted(cols_to_remove, reverse=True)
# Store the rows that have been seen in a list
row_seen = []
# Store the cleaned data
cleaned = []
# Store the total count
total_count = 0

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
            # Check the range & length of the storage list
            for i in range(len(row)):
                # If the value contains '/2022' remove it to be 'm/d' notation
                if str(row[i]).find('/2022') != -1:
                    row[i] = str(row[i]).replace('/2022', '')
            
            # Relabel the 'View By' column to blank
            if str(row[0]) == "View By":
                row[0] = ''
            # Check if the 'View By' column has been seen so it's not duplicated in the file
            elif row[0] in row_seen:
                continue
            else:
                # Add the 'View By' value to the row_seen list
                row_seen.append(row[0])
                # Enumerate over the cells:
                # Convert strings to floats, then ints
                # Change blank strings to 0's
                # Add each cell to the total_count

                # Skip the first row so it isn't processed
                if len(row_seen) > 1:
                    # Iterate through each cell in the row
                    for i, cell in enumerate(row):
                        # Skip the first cell
                        if i < 1: continue

                        # Convert any empty strings into 0
                        if cell == '':
                            cell = 0
                        # Remove any commas
                        # Convert any strings into floats and then ints
                        else:
                            cell = cell.replace(',', '')
                            cell = int(float(cell))
                        # Add the values to the running total
                        total_count = total_count + cell

                # Write the result to the file
                writer.writerow(row)

        # Add a final row with the total count
        final_row = ["Total", total_count]
        writer.writerow(final_row)
                
    print("File processed and saved as Cleaned_" + filename)
    