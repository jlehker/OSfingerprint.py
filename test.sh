#!/bin/sh
#!/bin/bash

#testing commit

# Tell the user what you're doing. Nobody with an ounce of caution
# should just randomly give out root access without knowing what
# it will be used for. Also, the su prompt simply says "Password",
# meaning the user needs to be told *which* password to enter
# (i.e. not their normal user account password)

echo "This script needs root access."
echo "Please enter root's password when prompted."

echo "\nOSfingerprint.py utsa.edu"
sudo python OSfingerprint.py utsa.edu

echo "\nOSfingerprint.py cs.utsa.edu"
sudo python OSfingerprint.py cs.utsa.edu

echo "\nOSfingerprint.py sefm.cs.utsa.edu"
sudo python OSfingerprint.py sefm.cs.utsa.edu

echo "\nOSfingerprint.py elk04.cs.utsa.edu"
sudo python OSfingerprint.py elk04.cs.utsa.edu

# Give up root access immediately after you're done performing the
# copies. This should return the process to a regular user
exit

# Perform any other cleanup tasks (as a non-privileged user)

# Exit with successful status
exit 0
