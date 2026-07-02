#!/usr/bin/python
import os
import OpenSSL
import requests

download_cert_URL = "https://dev.missilesys.com/download_cert"
settings_URL = "https://missilesys.com/settings"

# Create CSR

def create_csr(cn, ca, org, organizational_unit=False, country=False, state=False, city=False, email_address=False):

	key = OpenSSL.crypto.PKey()
	key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)
	req = OpenSSL.crypto.X509Req()
	#cert = OpenSSL.crypto.X509()

	subject = req.get_subject()
	subject.O = org
	subject.CN = cn
	subject.req_extensions = 'v3_ca'
	subject.DN = 'missilesys.com'
	req.add_extensions([OpenSSL.crypto.X509Extension("basicConstraints", True, "CA:TRUE")]) #, OpenSSL.crypto.X509Extension("subjectKeyIdentifier", False, b'hash')])

	req.set_pubkey(key)
	req.sign(key, 'sha256')
	'''
	cert.set_serial_number(1)
	cert.gmtime_adj_notBefore(0)
	cert.gmtime_adj_notAfter(60*60*24*365)
	cert.set_issuer(req.get_subject())
	cert.set_subject(req.get_subject())
	cert.set_pubkey(req.get_pubkey())
	cert.sign(pkey, 'sha256')
	'''
	private_key = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)
	csr = OpenSSL.crypto.dump_certificate_request(OpenSSL.crypto.FILETYPE_PEM, req)
	return private_key, csr

#

# Sends a request to dev.missilesys.com/download_cert using specified CSR

def certdownload(username, password, ca, org, outpath):
	privatekey, csr = create_csr(username,ca,org)
	#with open('csr'+outpath+'.txt', 'wb') as csrFile:
	#	csrFile.write(csr)
	#with open('privatekey'+outpath+'.key', 'wb') as pkFile:
	#	pkFile.write(privatekey)
	data = { 'username': username, 'password': password, 'privatekey': privatekey, 'csr': csr }
	r = requests.post(download_cert_URL, data=data, verify=False, stream=True)
	with open(outpath+'.p12', 'wb') as p12:
		for chunk in r.iter_content(chunk_size=128):
			p12.write(chunk)

if __name__ == "__main__":
	user = 'invalid'
	ca_file = 'ca-pkcs'
	org = 'International Weapons Export Inc.'
	certdownload(user, '123', True, org, ca_file) # Get the CA
