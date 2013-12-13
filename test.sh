#!/bin/bash

servers=( utsa.edu 
        cs.utsa.edu 
        sefm.cs.utsa.edu 
        elk04.cs.utsa.edu 
        localhost )

echo "This script needs root access."
echo "Please enter root's password when prompted."

for i in "${servers[@]}"
do
    printf "\nOSfingerprint.py $i\n"
    sudo python OSfingerprint.py $i
done

exit
