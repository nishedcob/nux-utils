#! /bin/sh

cd
find .ssh/ -type f -exec bash -c '(base64 -w 0 {} ; echo ""; base64 -w 0 {} ; echo "") | pass insert {}' \;
cd -

