'''https://github.com/AhmedCDU/Softwarenow.git'''

# Task 4 Part 2: Utilize BioBERT to separately extract 'diseases' and 'drugs' entities from the 'extracted_text.txt' file.

import biobert_ner as b_ner
import json

# Load the BioBERT NER model
model = b_ner.load_model('biobert_v1.1_pubmed')

# Read the extracted text
with open('extracted_text.txt', 'r') as file:
    text = file.read()

# Extract the entities
entities = model.predict(text)

# Display the diseases and drugs entities
print('Diseases:')
for entity in entities['diseases']:
    print(entity)

print('\nDrugs:')
for entity in entities['drugs']:
    print(entity)
