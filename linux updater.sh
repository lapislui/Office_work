#!/bin/bash
while [ true ] ;
do
    git add . 
    git commit -m "creation commit"
    git push
skip 1500;
done