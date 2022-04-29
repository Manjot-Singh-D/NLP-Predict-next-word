from src.chain import MarkovChain
import sys

def load_markov_chain(order):
    if order == "1":
        try:
            new_chain = MarkovChain.from_json('markov_chain_1st_order.json')
            print("loaded ok")
            return new_chain
        except (FileNotFoundError):
            print("Couldn't load the Markov Chain. File does not exist.")
            print("First train a Markov Chain and save it to a json file.")
            print("(see train1storder.py ) ")
            sys.exit(0)
    elif order == "2":
        try:
            new_chain = MarkovChain.from_json('markov_chain_2nd_order.json')
            print("loaded ok")
            return new_chain
        except (FileNotFoundError):
            print("Couldn't load the Markov Chain. File does not exist.")
            print("First train a Markov Chain and save it to a json file.")
            print("(see train2ndorder.py )")
            sys.exit(0)
    elif order == "3":
        try:
            new_chain = MarkovChain.from_json('markov_chain_3rd_order.json')
            print("loaded ok")
            return new_chain
        except (FileNotFoundError):
            print("Couldn't load the Markov Chain. File does not exist.")
            print("First train a Markov Chain and save it to a json file.")
            print("(see train3rdorder.py )")
            sys.exit(0)
    else:
        print("Wrong Input")
        print("Type 1 to load 1st order Markov Chain")
        print("Type 2 to load 2nd order Markov Chain")
        print("Type 3 to load 3rd order Markov Chain")
        sys.exit(0)

def predict_next_word(state, chain, order):
    if order == "1":
        print("... " + state[-1] + " ...")
        prediction = chain.find_next_state(state[-1])
        return prediction
    elif order == "2":
        print("... " + " ".join(state[-2:]) + " ...")
        prediction = chain.find_next_state(" ".join(state[-2:]))
        return prediction
    elif order == "3":
        print("... " + " ".join(state[-3:]) + " ...")
        prediction = chain.find_next_state(" ".join(state[-3:]))
        return prediction
    else:
        print("Something went wrong. Prediction failed")
      
def main(mar_type,text):
    typed = []
    quit = False

    order=str(mar_type)

    chain = load_markov_chain(order)
    while quit == False:
        word=text.split()
        typed.extend(word[:])
        if typed[-1] == 'q':
            quit = True
            break
        else:
            next_word = predict_next_word(typed,chain,order)
            return next_word
