#!/bin/bash

KEY_NAME=mongodb2.key

echo "generating $KEY_NAME"
openssl rand -base64 741 > $KEY_NAME

echo "setting permissions for mongo docker image"
echo "  file is only readable by owner: chmod 400"
chmod 400 $KEY_NAME

echo "  user/group is 999:999: chown 999:999"
chown 999:999 $KEY_NAME
echo "done"
