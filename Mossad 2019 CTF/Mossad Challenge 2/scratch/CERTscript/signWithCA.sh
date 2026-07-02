#!/bin/bash

openssl x509 -req -in administrator-csr -CA ca-cert.pem -CAkey ca-pk.key -out device.crt -set_serial 01 -days 500 -sha256
openssl pkcs12 -export -out administrator.p12 -inkey administrator-rsa.key -in device.crt -passout pass:"123"

