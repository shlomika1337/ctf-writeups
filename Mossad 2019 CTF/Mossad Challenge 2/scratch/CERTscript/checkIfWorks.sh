#!/bin/bash
./performAll.sh
./splitPKCS12.sh ca-pkcs.p12
curl -E ./ca-cert.pem --key ./ca-pk.key https://missilesys.com/
