#!/bin/bash
while [ true ] ;
do
    git add . 
    git commit -m "creation commit"
    git push
sleep 10
done