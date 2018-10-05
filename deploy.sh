#!/bin/bash

# Sample deploy script
#
# jonny.langefeld@gmail.com
#

display_usage() {
	cat <<EOF
Write a
multiline
help text here
EOF
	}

if [ "$#" -gt 0 ] || [ "$1" == '-h' ] || [ "$1" == '--help' ]
then
    display_usage
    exit 1
fi

echo 'execute deploy commands here'