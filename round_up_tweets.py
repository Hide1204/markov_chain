#ツイートを１つのテキストファイルにする
import json
import re
from data import search_list
from data import ignore_words
from pymongo import MongoClient

class Mongo:
    def __init__(self, collection_name,db_name="tweets_data"):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_many(self, documents):
        #print("pushing...")
        #print(documents)
        #print("***************")
        return self.collection.insert_many(documents)
    
    def get_datas(self):
        datas = list()
        for post in self.collection.find():
            datas.append(post)
        return datas

    def get_max_id(self):
        return self.collection.find_one(projection={"_id":0, "id": 1}, sort=[("id", -1)])

    def __del__(self):
        self.client.close()

def get_texts(collection_name):
    tweets_text = get_texts_list(collection_name)
    return remove_particular_string(tweets_text)

def get_texts_list(collection_name):
    db = Mongo(collection_name=collection_name)
    tweets = db.get_datas()
    tweets_text=list()
    for tweet in tweets:
        #print("***")
        #print(tweet['text'])
        tweets_text.append(tweet['text'])
    return tweets_text
    #print(tweets_text)

def remove_particular_string(tweets_text):
    tweets_text_after_process=[]
    for text in tweets_text:
        #print("***")
        #print(tweets_text['text'])
        flag = True
        for ignore_word in ignore_words.ignore_words:
            if re.search(re.escape(ignore_word["word"]),text):
                flag = False
                break
        if flag:
            tweets_text_after_process.append(text)
    return tweets_text_after_process

if __name__ == "__main__":
    main()
    #test()
