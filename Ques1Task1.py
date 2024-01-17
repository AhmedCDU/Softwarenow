'''Github repo.link https://github.com/AhmedCDU/Softwarenow.git'''


# Assignment 2, Question 1, Task 1: Extract text from multiple CSV files and consolidate them into a single '.txt' file
# Importing libraries
import csv
import os
import glob

# Save CSV files with "CSV" in their names in the current directory.
# Retrieve all CSV files in the current directory.
csv_files = glob.glob('CSV*.csv')
# Display the list of found CSV files in the directory.
print('The CSV files found in the directory are:', csv_files)

# Open a text file to write the extracted text.
with open('extracted_text.txt', 'w') as outfile:
    for csv_file in csv_files:
        # Open the CSV file.
        with open(csv_file, 'r') as infile:
            # Read the CSV file.
            reader = csv.reader(infile)

            # Iterate over the rows.
            for row in reader:
                # Write the row to the text file.
                outfile.write(','.join(row) + '\n')

print("The text file named 'extracted_text.txt' with the extracted text from CSV files has been saved in the current directory.")
