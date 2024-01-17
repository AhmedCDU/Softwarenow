'''github repo link https://github.com/AhmedCDU/Softwarenow.git'''

# Task 3.2: Using the 'Auto Tokenizer' function in the 'Transformers' library to create a 'function'
# that counts unique tokens in a text (.txt) file and provides the 'Top 30' words.

from transformers import AutoTokenizer

def count_tokens(text_file):
    with open(text_file, "r") as file:
        text = file.read()
    
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer.tokenize(text)
    unique_tokens = set(tokens)
    print("Number of unique tokens:", len(unique_tokens))
    
    # Sort unique tokens by frequency and select the top 30
    top_30_words = sorted(unique_tokens, key=lambda x: tokens.count(x), reverse=True)[:30]
    print("Top 30 words:", top_30_words)
