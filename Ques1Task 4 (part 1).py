'''github repo link https://github.com/AhmedCDU/Softwarenow.git'''

# Task 4: Utilize 'en_core_sci_sm' to extract 'diseases' and 'drugs' entities separately from the 'extracted_text.txt' file.

import spacy
import scispacy

nlp = spacy.load('en_core_sci_sm')

with open('extracted_text.txt', 'r') as file:
    text = file.read()

doc = nlp(text)

# Extract 'diseases' entities
diseases = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']

# Extract 'drugs' entities
drugs = [ent.text for ent in doc.ents if ent.label_ == 'DRUG']

# Display the extracted entities
print("Diseases:", diseases)
print("Drugs:", drugs)
