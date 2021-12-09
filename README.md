# rocketchat-DB-monitoring

Sample python script for monitoring Rocketchat database and get statistics of users.


**1. Update python:**
```
yum check-update && yum install python3 -y
pip3 install pymongo
pip3 install dotenv
pip3 install "python-dotenv[cli]"
```

**2. Go to the directory where script placed and run it.**
```
python3 rocketchat_db_query.py
```
