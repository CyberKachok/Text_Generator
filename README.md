# Text_Generator
A program that can predict the next word in a pseudo-sentence based on the previous words in the sequence and the data that is used to create a statistical model
1. Opens and reads the corpus from the provided file corpus.txt. 
2. Makes a list of trigrams. It consists of heads and tails, but heads consist of two space-separated tokens concatenated into a single string. The tails consist of one token. For example: head — winter is, tail — coming. The model trained based on the list of trigrams.
3. Chooses a random head from the corpus that will serve as the first word of the chain
4. The second word predicted by looking up the the concatenation of the last two tokens of the chain in the model and choosing the most probable next word from the set of possible follow-ups.
The sentences that are being generated:
— Start with capitalized words ("This is beautiful.", "You are a great programmer!", etc.);
— Do not start with a word that ends with a sentence-ending punctuation mark ("Okay.", "Nice.", "Good.", "Look!", "Jon!", etc.);
— End with a sentence-ending punctuation mark like ., !, or ?;
— Should not be shorter than 5 tokens.
5. Generates and prints 10 pseudo-sentences that meet these criteria. A pseudo-sentence ends when the first sentence-ending punctuation mark is encountered after the minimal sentence length (5 tokens) is reached.
