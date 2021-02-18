#!/bin/bash

today=$(date +"%Y/%m/%d")
last=$(head -n 1 .update_log.txt)
if [[ $today != $last ]]
then
	echo "Updating tickers, please wait"
	sh ./get_symbols.sh
	echo $today > .update_log.txt
	echo "Update finished"
fi
