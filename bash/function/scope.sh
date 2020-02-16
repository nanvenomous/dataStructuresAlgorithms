#!/bin/bash
a=2
doStuff() {
	a=3
}
doStuff
echo "${a}" # echoes 3
