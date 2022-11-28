#!/usr/bin/zsh

for (( i = 1; i <= 10; i++ )) do
    time (python3 main.py 1000 100 test.py) >> /dev/null
    rm -rf test.py
done
