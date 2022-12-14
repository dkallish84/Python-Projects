import csv, sys

# Check to see if a file was passed as an argument
try:
    filename = sys.argv[1]
except:
    # If no argument was passed, prompt for the filename
    filename = input("Enter the filename: ")

# Assumes first column is 'First Dimension'
cols_to_remove = [0]
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
            # Remove the specified column(s)
            for col_index in cols_to_remove:
                # Delete the column
                del row[col_index]
                # Write to the cleaned list
                cleaned.append(row)

        for row in cleaned:
            # Relabel 'View By' to '' and '' to 'Cases'
            if str(row[0]) == 'View By':
                row[0] = ''
            if str(row[1]) == '':
                row[1] = 'Cases'

            # Check if the 'View By' is already seen
            if row[0] in row_seen:
                continue
            else:
                # Add the 'View By' value to the row_seen list
                row_seen.append(row[0])
                
                # Column 1 (Cases) will contain the result of adding all other columns, 
                # 2 through the end of the row, together

                # Skip the first row, we don't want it processed
                if len(row_seen) > 1:
                    # Change 'Cases' to 0 after the first row
                    row[1] = 0

                    # Iterate through each cell in the row
                    for i, cell in enumerate(row):
                        # Skip the first two cells
                        if i < 2: continue

                        # Convert any empty strings into 0
                        if cell == '':
                            cell = 0
                        # Convert any strings into floats and then ints
                        else:
                            cell = cell.replace(',', '')
                            cell = int(float(cell))
                        # Add the values together and assign them to the Cases column
                        row[1] = row[1] + cell
                        # Add the value to the total count
                        total_count = total_count + cell

                # Write the result to the file
                writer.writerow(row)
        
        # Add a final row with the total count
        final_row = ["Total", total_count]
        writer.writerow(final_row)
    
    print("File processed and saved as Cleaned_" + filename)
