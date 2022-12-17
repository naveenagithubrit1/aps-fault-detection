import pymongo
import pandas as pd
import json

#This file is To dump data into mongo db

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME="aps"
COLLECTION_NAME="sensor"
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"

if __name__ == "__main__" :
    df= pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Converting dataFrame to json , so that we can dump into mongo db
    df.reset_index(drop=True , inplace=True)

    record_json = list(json.loads(df.T.to_json()).values())
    print(record_json[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(record_json)