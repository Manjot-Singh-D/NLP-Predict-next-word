from chain import MarkovChain
from nltk.corpus import gutenberg

mc = MarkovChain(2)

corpora_path = 'nltk_data/corpora/gutenberg/'

for filename in gutenberg.fileids():
    print(corpora_path+str(filename))
    try:
        mc.train(corpora_path+str(filename))
    except (UnicodeDecodeError):
        pass


# convert to json and save to file
mc.to_json('markov_chain_3rd_order.json')