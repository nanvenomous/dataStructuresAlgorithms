#!/bin/bash
# https://sookocheff.com/post/bash/parsing-bash-script-arguments-with-shopts/

# GetOpts parsing example
#	input string:
#		":ht" disables default error handling
#		"h:t" indicates the -h flag takes an argument

verbose=false

function echo_v() {
	if [ "${verbose}" = true ]; then
		echo "${@}"
	fi
}

while getopts ":hvt:" opt; do
	case ${opt} in
		h ) # process option a
			echo 'this is the help menu'
			;;
		t ) # process option t
			echo ${OPTARG}
			;;
		v ) # process option t
			verbose=true
			;;
		\? ) echo "Usage: cmd [-h] [-t]"
			;;
	esac
done

echo_v 'script is now verbose'
