#!/bin/bash

if [[ -f "webserver.pid" ]]; then
		echo webserver.pid  | xargs kill -15
		echo "Stopped webserver"
		rm "webserver.pid"

if [[ -f "scheduler.pid" ]]; then
    echo webserver.pid  | xargs kill -15
    echo "Stopped scheduler"
    rm "scheduler.pid"
