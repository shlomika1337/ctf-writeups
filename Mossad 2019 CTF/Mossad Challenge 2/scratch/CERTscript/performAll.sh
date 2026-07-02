#!/bin/bash
python Mossad2.py
./splitPKCS12.sh ca-pkcs.p12
./signWithCA.sh
./printPKCS12.sh administrator.p12
