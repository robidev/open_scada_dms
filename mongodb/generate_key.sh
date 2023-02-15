#!/bin/sh

KEY_NAME=mongodb.key

echo "generating $KEY_NAME"
openssl rand -base64 741 > $KEY_NAME

echo "setting permissions for mongo docker image"
echo "  file is only readable by owner: chmod 400"
chmod 700 $KEY_NAME

echo "  user/group is 999:999: chown 999:999"
chown 999:999 $KEY_NAME
echo "done"
