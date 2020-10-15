import re
import MeCab

import ignore_words
#from PrepareChain import PrepareChain
import round_up_tweets

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    return t.parse(text)

def main():
    pass

def test():
    tweet_data=round_up_tweets.test()
    for text in tweet_data:
        print(text)
        print(wakati(text))
    
if __name__ == "__main__":
    #main()
    test()