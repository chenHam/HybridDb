
#!/bin/bash

#execution example: ./exec.sh 5

for i in 'seq 1 $1';
do
    echo $i
    #exectue python script
    printf "test"
    python ./demo.py
done

