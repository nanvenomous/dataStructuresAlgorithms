#!/bin/bash

array=("item 1" "item 2" "item 3")
iter=0

for i in "${array[@]}"; do   # The quotes are necessary here
	echo "$i"

	echo "iterator: ${iter}"
	iter=$(expr ${iter} + 1)

	echo
done
