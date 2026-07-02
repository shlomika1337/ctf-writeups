# CTF Writeups

Writeups from cybersecurity competitions I have solved, covering reverse engineering, protocol exploitation, network attacks, cryptography, forensics, and steganography.

## Writeups

### Check Point Security Academy 2020
Multi-challenge writeup. The strongest challenge, **Shoes**, involved reverse engineering a custom SOCKS-like network protocol from packet captures: recovering the XOR key of a challenge-response scheme by diffing challenges across sessions, then modifying requests past a CRC-32 integrity check to redirect the proxy to an internal target. **CS-Hacked** was an end-to-end network attack: SSH access, reconnaissance, ARP-spoofing MITM, traffic capture, and recovery of an RC4 key via a length-correlated dictionary attack. Also includes DOC magic-byte forensics and steganography challenges.

### Hoshen / Sukkot 2020 (IDF Cyber Riddle)
A steganography chain: decoding Morse from shofar-audio to recover an IP address, extracting a password-protected RAR hidden inside a JPEG (binwalk), cracking the archive with John the Ripper and rockyou, and decoding a payload image whose pixel hex values spell out the flag.

## Notes

- Writeups are provided as PDF so they render inline with their screenshots.
- These document challenges from public recruitment/community CTFs.
