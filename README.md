# forensicpy
Library for performing mobile device decoding for nibbles and 7-bit decoding
-
7-bit and reverse 7-bit is a popular encoding format for SMS messages with GSM. The concept was that the user portion of an SMS holds encoded text data. When 7 bits of binary data is packed in an octet (8 bits) it requires unpacking. The process is that the least significant bit from the next 7-bits is actually added to the current one being packed. 

Packing
1) Convert text into 7-bits using the hex representation of the 7-bits
2) Move the LSB from the next 7-bits to the current one being packed
3) Pad the last byte with 0's

To unpack, reverse the process
