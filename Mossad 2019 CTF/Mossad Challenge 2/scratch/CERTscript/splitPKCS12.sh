#!/bin/bash
openssl pkcs12 -in $1 -nocerts -out ca-pk.key -passin pass:"123" -nodes
openssl pkcs12 -in $1 -clcerts -nokeys -out ca-cert.pem -passin pass:"123" -nodes
