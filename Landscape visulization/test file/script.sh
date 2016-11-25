#!/bin/bash

for i in {1..1000000}
do
	echo "$(($RANDOM%100000000)) $(($RANDOM%100000000))" >> newfile.txt
done
