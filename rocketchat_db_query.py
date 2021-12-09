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
def _openFile(_env:str): #Output File
  ABS_PATH = _getEnv("OUTPUT_PATH")
  if _env == "output_online_users":
    FILE_NAME = "online_users.prom"
    ONLINE_USERS_OUTPUT = open(file= ABS_PATH + FILE_NAME, mode="w")
    _msg = "online user query wrote to output."
    _logger(_msg)
    return (ONLINE_USERS_OUTPUT)
  elif _env == "output_busy_users":
    FILE_NAME = "busy_users.prom"
    BUSY_USESR_OUTPUT = open(file= ABS_PATH + FILE_NAME, mode="w")
    _msg = "busy user query wrote to output."
    _logger(_msg)
    return (BUSY_USESR_OUTPUT)
  elif _env == "output_away_users":
    FILE_NAME = "away_users.prom"
    AWAY_USERS_OUTPUT = open(file= ABS_PATH + FILE_NAME, mode="w")
    _msg = "away user query wrote to output."
    _logger(_msg)
    return (AWAY_USERS_OUTPUT)
  elif _env == "output_offline_users":
    FILE_NAME = "offline_users.prom"
    OFFLINE_USERS_OUTPUT = open(file= ABS_PATH + FILE_NAME, mode="w")
    _msg = "offline user query wrote to output."
    _logger(_msg)
    return (OFFLINE_USERS_OUTPUT)
  elif _env == "output_total_sent_msg":
    FILE_NAME = "total_sent_msgs.prom"
    SENT_MSG_OUTPUT = open(file= ABS_PATH + FILE_NAME, mode="w")
    _msg = "sent msg query wrote to output."
    _logger(_msg)
    return (SENT_MSG_OUTPUT)
  elif _env == "output_total_uploaded_docs":
    FILE_NAME = "total_uploade_docs.prom"
    UPLOAD_DOCS_OUTPUT = open(file= ABS_PATH + FILE_NAME, mode="w")
    _msg = "attachment query wrote to output."
    _logger(_msg)
    return (UPLOAD_DOCS_OUTPUT)
  elif _env == "output_total_rooms":
    FILE_NAME = "total_rooms.prom"
    TOTAL_ROOMS_OUTPUT = open(file= ABS_PATH + FILE_NAME, mode="w")
    _msg = "rooms query wrote to output."
    _logger(_msg)
    return (TOTAL_ROOMS_OUTPUT)
  else:
    pass
#--------------------------------------------------------
# Get Environments
def _getEnv(_env:str):
  load_dotenv()
  if _env == "REPLICA_SET":
    _replicaSetENV = os.getenv("REPLICA_SET")
    return (_replicaSetENV)
  elif _env == "COLLECTION_USERS":
    _collectionUsersENV = os.getenv("COLL_USERS")
    return (str(_collectionUsersENV))
  elif _env == "COLLECTION_MSGS":
    _collectionMsgsENV = os.getenv("COLL_MSGS")
    return (_collectionMsgsENV)
  elif _env == "COLLECTION_UPLOADS":
    _collectionUploads = os.getenv("COLL_UPLOADS")
    return (_collectionUploads)
  elif _env == "COLLECTION_ROOMS":
    _collectionRooms = os.getenv("COLL_ROOMS")
    return (_collectionRooms)
  elif _env == "LOG_FILE":
    _logFile = os.getenv("LOG_FILE")
    return (_logFile)
  elif _env == "OUTPUT_PATH":
    _outputpath = os.getenv("OUTPUT_PATH")
    return (str(_outputpath))
  else:
    pass
#--------------------------------------------------------
# Open Mongo Connection
def _mongoConnection(_coll:str):
  MONGODB_URI = _getEnv("REPLICA_SET")
  MONGO_CLIENT = MongoClient(MONGODB_URI)
  DATABASE = MONGO_CLIENT.rocketchat
  if _coll == "USERS":
    COLLECTION = DATABASE[_getEnv("COLLECTION_USERS")]
    return (COLLECTION)
  elif _coll == "MSGS":
    COLLECTION = DATABASE[_getEnv("COLLECTION_MSGS")]
    return (COLLECTION)
  elif _coll == "UPLOADS":
    COLLECTION = DATABASE[_getEnv("COLLECTION_UPLOADS")]
    return (COLLECTION)
  elif _coll == "ROOM":
    COLLECTION = DATABASE[_getEnv("COLLECTION_ROOMS")]
    return (COLLECTION)
  else:
    pass
#--------------------------------------------------------
def _countOnlineUsers():
  QUERY = _mongoConnection("USERS").count_documents({"status": "online"}) #Count Online Users
  _msg = "query execution. online user count queried"
  _logger(_msg)
  return (QUERY)
#--------------------------------------------------------
def _countBusyUsers():
  QUERY = _mongoConnection("USERS").count_documents({"status": "busy"}) #Count Busy Users
  _msg = "query execution. busy user count queried"
  _logger(_msg)
  return (QUERY)
#--------------------------------------------------------
def _countAwayUsers():
  QUERY = _mongoConnection("USERS").count_documents({"status": "away"}) #Count Away Users
  _msg = "query execution. away user count queried"
  _logger(_msg)
  return (QUERY)
#--------------------------------------------------------
def _countOffLineUsers():
  QUERY = _mongoConnection("USERS").count_documents({"status": "offline"}) #Count OffLine Users
  _msg = "query execution. offline user count queried"
  _logger(_msg)
  return (QUERY)
#--------------------------------------------------------
def _countSentMsgs():
  QUERY = _mongoConnection("MSGS").count_documents({}) #Count Total Sent Messages
  _msg = "query execution. total msg count queried"
  _logger(_msg)
  return (QUERY)
#--------------------------------------------------------
def _countTotalUploads():
  QUERY = _mongoConnection("UPLOADS").count_documents({}) #Count Total Uploaded Docs
  _msg = "query execution. total attachment count queried"
  _logger(_msg)
  return (QUERY)
#--------------------------------------------------------
def _countRooms():
  QUERY = _mongoConnection("ROOM").count_documents({}) #Count Total Rooms
  _msg = "query execution. total room count queried"
  _logger(_msg)
  return (QUERY)
#--------------------------------------------------------
def main(): # Main script

  _msg = "Bingo! script started..."
  _logger(_msg)
  
  onlineUsers = _countOnlineUsers()
  busyUsers = _countBusyUsers()
  awayUsers = _countAwayUsers()
  offLineUsers = _countOffLineUsers()
  countSentMsg = _countSentMsgs()
  countUploads = _countTotalUploads()
  countRooms = _countRooms()

  print("Total_Online_Users:", onlineUsers, file=_openFile("output_online_users"))
  print("Total_Busy_Users:", busyUsers, file=_openFile("output_busy_users"))
  print("Total_Away_Users:", awayUsers, file=_openFile("output_away_users"))
  print("Total_Offline_Users:", offLineUsers, file=_openFile("output_offline_users"))
  print("Total_Sent_Messages:", countSentMsg, file=_openFile("output_total_sent_msg"))
  print("Total_Uploaded_Documents:", countUploads, file=_openFile("output_total_uploaded_docs"))
  print("Total_Rooms:", countRooms, file=_openFile("output_total_rooms"))

  _msg = "Script execution finished!"
  _logger(_msg)
#--------------------------------------------------------
if __name__ == "__main__": # Execution
  main()