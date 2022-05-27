# Add libraries

from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

#--------------------------------------------------------
#logging
def _logger(_env:str):
  _log_format = "%(asctime)s %(levelname)s %(message)s"
  logging.basicConfig(filename=_getEnv("LOG_FILE"), filemode='w', level=logging.INFO, format=_log_format)
  logging.info(_env)
#--------------------------------------------------------
def _getEnv(_env:str):
  load_dotenv()
  if _env == "REPLICA_SET":
    _replicaSetENV = os.getenv("REPLICA_SET")     # Respond the MongoDB ReplicaSet connection string
    return (_replicaSetENV)
#--------------------------------------------------------
def _queryAbuseApps():      # Finding Users whome installed none-FairChat Application Tokens
  MONGODB_URI = _getEnv("REPLICA_SET")
  MONGO_CLIENT = MongoClient(MONGODB_URI)
  DATABASE = MONGO_CLIENT["rocketchat"]
  COLL = DATABASE["_raix_push_app_tokens"]
  QUERY = ({"appName" : {"$nin" : ["com.osalliance.rocketchatMobile", "com.osalliance.RocketchatMobile","com.osalliance.RocketChatMobile","chat.rocket.reactnative"]}})
  DOCUMENT = COLL.find(QUERY,{"appName":1,"userId":1}).sort("appName")
  USERID = []
  for item in DOCUMENT:
    USERID.append(item["userId"])
  return (USERID)
#--------------------------------------------------------
def _findAbuseUsers(USERID: str):     # Finding UsersIDs,Names,Emails whome installed none-FairChat Application 
  MONGODB_URI = _getEnv("REPLICA_SET")
  MONGO_CLIENT = MongoClient(MONGODB_URI)
  DB = MONGO_CLIENT.get_database(name="rocketchat")
  COLLECTION_NAMES = DB.list_collection_names()
  for item in COLLECTION_NAMES:
    if item == "users":
      USERS_COLLECTION = DB.get_collection(name=item)
      QUERY = {"_id":{"$in":[USERID]}}
      DOCUMENT = USERS_COLLECTION.find(QUERY,{"username":1,"name":1,"emails.address":1,"_id":0}).sort("_id")
      abusersAppList = []
      for item in DOCUMENT:
        abusersAppList.append(item["emails"]) #return just user's names
        return(abusersAppList)
#--------------------------------------------------------
if __name__ == "__main__":      # Execution part
  resultAbuseApps = _queryAbuseApps()
  for item in resultAbuseApps:
    abuserfind = _findAbuseUsers(str(item)) 
    print(abuserfind,end="\n")
