'''
/**
 * Copyright (c) 2017, Jack Mo (mobangjack@foxmail.com).
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
'''

'''
/** 
* Number System Converter
*/
'''

# Digits system
class Digits:

	# Get symbolic digits (tuple)
	def symbolic(self):
		array = []
		for i in range(ord('0'), ord('9') + 1):
			array.append(chr(i))
		for i in range(ord('a'), ord('z') + 1):
			array.append(chr(i))
		return tuple(array)

	# Get numerical digits (dictionary)
	def numerical(self):
		dic = {}
		sym = self.symbolic()
		for i in range(0, len(sym)):
			dic[sym[i]] = i
		return dic

	# Constructor
	def __init__(self):
		self.sym = self.symbolic()
		self.num = self.numerical()
	
	# Symbolic access
	def at(self, idx):
		return self.sym[idx]
	
	# Numerical access
	def of(self, sym):
		return self.num[sym]

# Number system convertor
class Converter:

	# Convert any number system to decimal
	def any2dec(self, symbols, base):
		decimal = 0
		weight = 1
		for symbol in symbols[::-1]:
			number = self.digits.of(symbol)
			decimal = decimal + number * weight
			weight = weight * base
		return decimal

	# Convert decimal to any number system
	def dec2any(self, decimal, base):
		quotient = decimal / base
		remainder = decimal % base
		result = ''
		while (quotient != 0) :
			result = result + self.digits.at(remainder)
			remainder = quotient % base
			quotient = quotient / base
		result = result + self.digits.at(remainder)
		return result[::-1]

	# Convert number system from any to any
	def any2any(self, src, src_base, dst_base):
		dec = self.any2dec(src, src_base)
		ret = self.dec2any(dec, dst_base)
		return ret

	# Constructor
	def __init__(self):
		self.digits = Digits()

# Say hello
def say_hello():
	print
	print("   *******  ********    ******  \n  **** ***  ****  ***  ***  *** \n  ***   *** ****  ***  ***      \n ****       ***   ***  *****    \n ****       ***   ***    ****** \n ****   *** ***   ***       *** \n  ***  **** ***   ***  ***  *** \n  ********  ***   ***  ******** \n    *****   ***   ***   ******  ")
	print

# Main entrance
if __name__ == "__main__":

	# say hello
	say_hello()

	# use converter
	converter = Converter()

	# use argparse to parse arguments
	import argparse
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--input", required=True, help="Input number, e.g. 123456789abc")
	ap.add_argument("-f", "--from_base", required=True, help="Base of input number, e.g. c")
	ap.add_argument("-t", "--to_base", required=True, help="Base of output number, e.g. z")
	args = vars(ap.parse_args())

	input_symbols = str(args["input"])
	from_base = converter.digits.of(args["from_base"]) + 1
	to_base = converter.digits.of(args["to_base"]) + 1

	# Convert
	output_symbols = converter.any2any(input_symbols, from_base, to_base)

	# print result
	print output_symbols

