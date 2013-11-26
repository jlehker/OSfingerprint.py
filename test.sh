#!/bin/bash

# Tell the user what you're doing. Nobody with an ounce of caution
# should just randomly give out root access without knowing what
# it will be used for. Also, the su prompt simply says "Password",
# meaning the user needs to be told *which* password to enter
# (i.e. not their normal user account password)
servers=( utsa.edu 
        cs.utsa.edu 
        sefm.cs.utsa.edu 
        elk04.cs.utsa.edu 
        slavin.info )

echo "This script needs root access."
echo "Please enter root's password when prompted."

for i in "${servers[@]}"
do
    printf "\nOSfingerprint.py $i"
    sudo python OSfingerprint.py $i
done

exit

# Perform any other cleanup tasks (as a non-privileged user)

# Exit with successful status
exit 0
