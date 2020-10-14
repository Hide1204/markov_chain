#ツイートを１つのテキストファイルにする
import json
from data import search_list
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

def main():
    pass

def test():
    db = Mongo(collection_name="Hide1204_")
    tweets = db.get_datas()
    tweets_text=list()
    for tweet in tweets:
        print("***")
        print(tweet['text'])
        tweets_text.append(tweet['text'])
    #print(tweets_text)
    
if __name__ == "__main__":
    #main()
    test()
