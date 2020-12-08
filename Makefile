start-local:
	export AIRFLOW_HOME=.
	airflow webserver & > webserver.txt
	echo "$!" > webserver.pid
	airflow scheduler & > scheduler.txt
	echo "$!" > scheduler.pid

stop-local:
	if [[ -f "webserver.pid" ]]; then
		echo webserver.pid  | xargs kill -15
		echo "Stopped webserver"
		rm "webserver.pid"
	if [[ -f "scheduler.pid" ]]; then
		echo webserver.pid  | xargs kill -15
		echo "Stopped scheduler"
		rm "scheduler.pid"

