'''
Script Name: forensicpy.py
Version: 2
Revised Date: 07/11/2015
Python Version: 3
Description: A module for performing mobile device decoding for nibbles and 7-bit encoding.
Copyright: 2014 Mike Felch <mike@linux.edu> 
URL: http://www.forensicpy.com/
--
- ChangeLog -
v2 - [07-11-2015]: Reverse 7-bit decoding bug fix
v1 - [11-05-2014]: Rewrite of the original code by John T
'''

def reverse_seven_bit_decode(bytes):
    '''
    Convert bytes from a reverse 7-bit string to a standard string.
    '''
    byte = [byte for byte in bytes]
    offset = 0
    bitmask = 0
    length = len(byte)
    decoded = bytearray()

    while True:
        if offset == length:
        	break

        if bitmask == 0:
        	decoded.append(                                    byte[offset] & 0x7F        )
        if bitmask == 1:
        	decoded.append( ((byte[offset-1] & 0x80) >> 7) | ((byte[offset] & 0x3F) << 1) )
        if bitmask == 2:
        	decoded.append( ((byte[offset-1] & 0xC0) >> 6) | ((byte[offset] & 0x1F) << 2) )
        if bitmask == 3:
        	decoded.append( ((byte[offset-1] & 0xE0) >> 5) | ((byte[offset] & 0x0F) << 3) )
        if bitmask == 4:
        	decoded.append( ((byte[offset-1] & 0xF0) >> 4) | ((byte[offset] & 0x07) << 4) )
        if bitmask == 5:
        	decoded.append( ((byte[offset-1] & 0xF8) >> 3) | ((byte[offset] & 0x03) << 5) )
        if bitmask == 6:
        	decoded.append( ((byte[offset-1] & 0xFC) >> 2) | ((byte[offset] & 0x01) << 6) )
        if bitmask == 7:
        	offset -= 1
        if bitmask == 7:
        	decoded.append(                                  ((byte[offset] & 0xFE) >> 1) )

        bitmask += 1
        bitmask = bitmask % 8
        offset += 1

    return decoded.decode('utf-8')

def seven_bit_decode(bytes):
	'''
	Converts 7-bit encoding to a string.
	'''
	bitmask = 0
	begin = 0
	end = 0
	decoded = bytearray()

	while True:
		if begin + 1 == len(bytes):
			break

		if bitmask == 0:
			decoded.append((bytes[begin] & 254) >> 1)

		if bitmask == 1:
			decoded.append((int.from_bytes(bytes[begin:end], byteorder='big') & 508) >> 2)

		if bitmask == 2:
			decoded.append((int.from_bytes(bytes[begin:end], byteorder='big') & 1016) >> 3)

		if bitmask == 3:
			decoded.append((int.from_bytes(bytes[begin:end], byteorder='big') & 2032) >> 4)

		if bitmask == 4:
			decoded.append((int.from_bytes(bytes[begin:end], byteorder='big') & 4064) >> 5)

		if bitmask == 5:
			decoded.append((int.from_bytes(bytes[begin:end], byteorder='big') & 8128) >> 6)

		if bitmask == 6:
			decoded.append((int.from_bytes(bytes[begin:end], byteorder='big') & 16256) >> 7)

		if bitmask == 7:
			decoded.append((bytes[begin] & 127) >> 0)

		if bitmask:
			begin += 1
			end = begin + 2

		bitmask += 1
		bitmask = bitmask % 8

	return decoded.decode('utf-8')

def nibbles_to_numbers(bytes):
	'''
	Convert bytes from nibbles to a string of numbers (commonly used for telephone numbers).
	'''
	numbers = ''
	ba = bytearray(bytes)
	for byte in ba:
		numbers += str((byte & 240) >> 4)
		numbers += str((byte & 15))
	return numbers

def reverse_nibbles_to_numbers(bytes):
	'''
	Convert bytes from reverse nibbles to a string of numbers (commonly used for telephone numbers).
	'''
	numbers = ''
	ba = bytearray(bytes)
	for byte in ba:
		numbers += str((byte & 15))
		numbers += str((byte & 240) >> 4)
	return numbers

def flip_nibbles(byte):
	'''
	Flips a nibble
	'''
	left = (byte & 240)
	left = left >> 4
	right = (byte & 15)
	right = right << 4

	return left | right

def string_nibbles_to_numbers(bytes):
	'''
	Convert a string of nibbles into numbers
	'''
	newtel = ''
	for i in bytes:
		newtel += hex(i)[2:]
	return newtel
