#!/bin/sh

PROCESS="waitress-serve"
PROCANDARGS="waitress-serve --host=0.0.0.0 --port=8080 --call 'project:create_app'"

while :
do
    RESULT=`pgrep ${PROCESS}`

    if [ "${RESULT:-null}" = null ]; then
            echo "${PROCESS} not running, starting " & exec waitress-serve --host=0.0.0.0 --port=8080 --call 'project:create_app'
    else
            echo "running"
    fi
    sleep 10
done
