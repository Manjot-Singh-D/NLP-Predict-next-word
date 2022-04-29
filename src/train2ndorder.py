from chain import MarkovChain
from nltk.corpus import gutenberg

mc = MarkovChain(1)

corpora_path = 'nltk_data/corpora/gutenberg/'

for filename in gutenberg.fileids():
    print(corpora_path+str(filename))
    try:
        mc.train(corpora_path+str(filename))
    except (UnicodeDecodeError):
        pass

mc.to_json('markov_chain_2nd_order.json')