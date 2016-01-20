#!/usr/bin/python
#!coding=utf8
import math

class Fences(object):
	"""
	docstring for Fences
	Fences cipher encode and decode
	"""
	def __init__(self, arg):
		super(Fences, self).__init__()
		self.arg = arg

	@staticmethod
	def encode(text,key):
		group=[]
		for i in xrange(0,key):
			group.append('')
		for i in xrange(0,len(text)):
			j=i%key
			group[j]=group[j]+text[i]

		s=''
		for i in xrange(0,key):
			s=s+group[i]
		return s

	@staticmethod
	def decode(text,key):
		gs=int(math.ceil(len(text)*1.0/key))
		group=[]
		for x in xrange(0,gs):
			group.append("")
		mo=len(text)%key
		for i in xrange(0,len(text)):
			if i<gs*mo:
				group[i%gs]+=text[i]
			else:
				j=i-gs*mo
				group[j%(gs-1)]+=text[i]
		s=''
		for i in group:
			s+=i
		return s