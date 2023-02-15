#!/bin/sh

SECRET_BYTE_LENGTH=48
INPUT_TEMPLATE="env.template"
OUTPUT=".env"
GRAFANA_CONFIG=./grafana/datasources/automatic.yaml

# generate url-safe random tokens
MONGODB_ROOT_PASSWORD=$( openssl rand $SECRET_BYTE_LENGTH | basenc --base64url )
MONGODB_PASSWORD=$( openssl rand $SECRET_BYTE_LENGTH | basenc --base64url )
REDIS_PASSWORD=$( openssl rand $SECRET_BYTE_LENGTH | basenc --base64url )
INFLUXDB_TOKEN=$( openssl rand $SECRET_BYTE_LENGTH | basenc --base64url )

echo "replacing secrets in $OUTPUT"
sed -e "s;%mongodb_password%;$MONGODB_PASSWORD;g" -e "s;%redis_password%;$REDIS_PASSWORD;g" -e "s;%influxdb_token%;$INFLUXDB_TOKEN;g" -e "s;%mongodb_root_password%;$MONGODB_ROOT_PASSWORD;g" $INPUT_TEMPLATE > $OUTPUT

echo "replacing influxdb secret in grafana datasource file: $GRAFANA_CONFIG"
sed -i -e "/token:/ s/: .*/: $INFLUXDB_TOKEN/" $GRAFANA_CONFIG
