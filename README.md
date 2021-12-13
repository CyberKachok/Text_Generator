# Text_Generator
Program that can predict the next word in a pseudo-sentence based on the previous words in the sequence and the data that is used to create a statistical model
1. Open and read the corpus from the provided file corpus.txt. The filename should be specified as user input. Note that the file is written in UTF-8 encoding, and the file should be in the same folder as your Python script.
2. Make a list of trigrams. It should consist of heads and tails, but heads should consist of two space-separated tokens concatenated into a single string. The tails should consist of one token. For example: head — winter is, tail — coming. The model should be trained based on the list of trigrams.
3. Choose a random head from the corpus that will serve as the first word of the chain
4. The second word should be predicted by looking up the the concatenation of the last two tokens of the chain in the model and choosing the most probable next word from the set of possible follow-ups.
The sentences that are being generated should:
— always start with capitalized words ("This is beautiful.", "You are a great programmer!", etc.);
— not start with a word that ends with a sentence-ending punctuation mark ("Okay.", "Nice.", "Good.", "Look!", "Jon!", etc.);
— always end with a sentence-ending punctuation mark like ., !, or ?;
— should not be shorter than 5 tokens.
5. Generate and print exactly 10 pseudo-sentences that meet these criteria. A pseudo-sentence should end when the first sentence-ending punctuation mark is encountered after the minimal sentence length (5 tokens) is reached.
