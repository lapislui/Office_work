#!/bin/bash
while [ true ] ;
do
    git add . 
    git commit -m "$(date)"
    git push
sleep 10
done