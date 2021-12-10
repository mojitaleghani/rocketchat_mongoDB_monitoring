# rocketchat-DB-monitoring

Sample python script for monitoring Rocketchat database and get statistics of users.


**1. Update python:**
```
yum check-update && yum install python3 -y
pip3 install pymongo
pip3 install dotenv
pip3 install "python-dotenv[cli]"
```
**2. Update the .env file with your appropriate MongoDB replicaset IP and port.**

**3. Go to the directory where script placed and run it.**
```
python3 rocketchat_db_query.py
```

*Grafana Dashboard*
![Grafana Dashboard](https://grafana.com/api/dashboards/15364/images/11401/image)
![Grafana Dashboard](https://grafana.com/api/dashboards/15364/images/11397/image)
