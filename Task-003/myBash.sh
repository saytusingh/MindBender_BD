#!/bin/bash

result=$(jps)

echo "${result}"

if [[ $result == *"ResourceManager"* ]];

	echo "It is active"

then
	eval "start-all.sh"

fi
