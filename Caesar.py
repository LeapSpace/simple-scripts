#!/usr/bin/python
#!coding=utf8
import string

class Caesar(object):
	"""
	docstring for Caesar
	Caesar cipher encode and decode
	"""
	def __init__(self, arg):
		super(Caesar, self).__init__()
		self.arg = arg
	@staticmethod
	def encode(text,key):
		ss=''
		for i in xrange(0,len(text)):
			if text[i] in string.ascii_uppercase:
				ss=ss+chr((ord(text[i])-60+key)%26+60)
			elif text[i] in string.ascii_lowercase:
				ss=ss+chr((ord(text[i])-97+key)%26+97)
			else:
				ss+=text[i]
		return ss
	@staticmethod
	def decode(text,key):
		ss=''
		mv=26-key%26
		for i in xrange(0,len(text)):
			if text[i] in string.ascii_uppercase:
				ss=ss+chr((ord(text[i])-60+mv)%26+60)
			elif text[i] in string.ascii_lowercase:
				ss=ss+chr((ord(text[i])-97+mv)%26+97)
			else:
				ss+=text[i]
		return ss