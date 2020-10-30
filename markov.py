import re
import MeCab
import random
import pickle
from collections import deque
from data import search_list

import round_up_tweets

max_len = 3

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    return t.parse(text)

def main():
    pass

def make_model(tweet_data):
    model={}
    tweet_data
    queue = deque([],max_len)
    queue.append("[BOS]")
    for markov_value in tweet_data:
        markov_value = wakati(markov_value)
        wakati_text_list = markov_value.split(' ')
        for markov in wakati_text_list:
            if queue[-1] == "\n":
                markov_key = tuple(queue)
                if markov_key not in model:
                    model[markov_key] = []
                model[markov_key].append("[BOS]")
                queue = deque([],max_len)
                queue.append("[BOS]")
            markov_key = tuple(queue)
            if markov_key not in model:
                model[markov_key]=[]
            model[markov_key].append(markov)
            queue.append(markov)
    return model

def make_sentence(model):
    value_list = []
    queue = deque([], max_len)
    queue.append("[BOS]")
    key = tuple(queue)
    while(True):
        key = tuple(queue)
        value = random.choice(model[key])
        if value == "\n":
            break
        value_list.append(value)
        queue.append(value)
    return value_list

def test():
    for user in search_list.search_list:
        tweet_data=round_up_tweets.get_texts(user["user_screan_name"])
        model = make_model(tweet_data)
        print("------"+user["user_screan_name"]+"------")
        for i in range(0, 1000):
            sentence = ''.join(make_sentence(model))
            print(sentence)
        #print(tweet_data)
    

if __name__ == "__main__":
    #main()
    test()
