#!/bin/bash

str='some.h'

echo "${str: -2}"

if [ ! "${str: -2}" == ".c" ] && [ ! "${str: -2}" == ".h" ]; then
	echo "Must pass in a source C or C++ file"
else
	echo "It worked"
fi
