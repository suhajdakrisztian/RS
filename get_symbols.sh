#!/bin/bash
curl -s ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt | cut -d"|" -f1 > ".nasdaq.txt"
curl -s ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt | cut -d"|" -f1 > ".nyse.txt"
sed -i "$ d" nasdaq.txt
sed -i "$ d" nyse.txt