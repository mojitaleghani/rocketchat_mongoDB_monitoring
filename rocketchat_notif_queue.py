# Add libraries

from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging
#--------------------------------------------------------
# Logging
def _logger(_env:str):
  _log_format = "%(asctime)s %(levelname)s %(message)s"
  logging.basicConfig(filename=_getEnv("LOG_FILE"), filemode='w', level=logging.INFO, format=_log_format)
  logging.info(_env)
#--------------------------------------------------------
# Output file
def _openFile(_env:str): #Output File
  ABS_PATH = _getEnv("OUTPUT_PATH")
  if _env == "output_notification_queue":
    FILE_NAME = "output_notification_queue.prom"
    NOTIFICATION_QUEUE_SIZE = open(file= ABS_PATH + FILE_NAME, mode="w")
    return (NOTIFICATION_QUEUE_SIZE)

#--------------------------------------------------------
# Get Environments
def _getEnv(_env: str):
  load_dotenv()
  if _env == "URI":
    _replicaSet = os.getenv("REPLICA_SET")
    return (str(_replicaSet))
  elif _env == "NotifQueue":
    COLLECTION = os.getenv("COLL_NOTIFQUEUE")
    return (str(COLLECTION))
  elif _env == "OUTPUT_PATH":
    _outputpath = os.getenv("OUTPUT_PATH")
    return (str(_outputpath))
  else:
    pass
#--------------------------------------------------------
# Run query
def notifQueueSize():
  QUERY = _mongoConnection("NotifQueue").count_documents({})
  if QUERY <= 250:
    return (QUERY)
  elif QUERY > 250:
    _mongoConnection("NotifQueue").delete_many({})
    return (QUERY)
#--------------------------------------------------------

def _abuseTokenApp(): #Count Abuse Application users
  CLIENT = MongoClient(_getEnv("REPLICA_SET"))
  DB = CLIENT.get_database(name="rocketchat")
  COLLECTION_NAMES = DB.list_collection_names()
  for item in COLLECTION_NAMES:
      if item == "_raix_push_app_tokens":
          TOKEN_COLLECTION = DB.get_collection(name=item)
          QUERY = ({"appName" : {"$nin" : ["com.osalliance.rocketchatMobile", "com.osalliance.RocketchatMobile","com.osalliance.RocketChatMobile","chat.rocket.reactnative"]}})
          RESULT = TOKEN_COLLECTION.count_documents(filter=QUERY)
          # return(RESULT)
          print(RESULT)

#--------------------------------------------------------
# Create mongo connection
def _mongoConnection(_env: str):
  MONGO_CLIENT = MongoClient(_getEnv("URI"))
  DATABASE = MONGO_CLIENT.rocketchat
  COLLECTION = DATABASE[_getEnv("NotifQueue")]
  return (COLLECTION)

#--------------------------------------------------------
# Main script
def main():
  # notificationQueueSize = notifQueueSize()
  deleteAbuseToken = _abuseTokenApp()

  print("Total_Notification_Queue_Size:", notificationQueueSize, file=_openFile("output_notification_queue"))
#--------------------------------------------------------

# Execution
if __name__ == "__main__":
  main()
