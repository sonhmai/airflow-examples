#!/bin/bash

if [[ -f "webserver.pid" ]]; then
		cat webserver.pid | xargs kill -15
		echo "Stopped webserver"
		rm "webserver.pid"
fi

if [[ -f "scheduler.pid" ]]; then
    cat scheduler.pid  | xargs kill -15
    echo "Stopped scheduler"
    rm "scheduler.pid"
fi

