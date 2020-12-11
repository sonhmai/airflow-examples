export AIRFLOW_HOME=./airflow
airflow initdb

# start webserver
airflow webserver -p 8080 > webserver.log 2>&1 &
PID=$!
echo $PID > webserver.pid

# scheduler
airflow scheduler > scheduler.log 2>&1 &
PID=$!
echo $PID > scheduler.pid
