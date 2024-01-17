'''github repo link https://github.com/AhmedCDU/Softwarenow.git'''


# Qsn 1 task 3.1 : Using any in-built library present in Python, count the occurrences of the words  in the text (.txt) and give the ‘Top 30’ most common words consist of letter. The code should not count special character as a word.  And store the ‘Top 30’ common words and their counts into a CSV file.


import re
import csv
from collections import Counter

# Read the text file
with open('extracted_text.txt', 'r') as file:
    text = file.read()

# Remove special characters
text = re.sub('[^A-Za-z\\s]', '', text)

# Split the text into words
words = text.split()

# Count the occurrences of each word
word_counts = Counter(words)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Write the top 30 words and their counts to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Count'])
    for word, count in top_30_words:
        writer.writerow([word, count])
