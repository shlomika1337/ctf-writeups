#!/bin/bash
openssl pkcs12 -in $1 -nodes -passin pass:123
