import os
import re
import sys
import time

from itertools import islice
from ZODB import FileStorage, DB

import zc.bz2storage
import transaction


class ZODBuffer():
	#	The goal is to split the data between the different database files
	#	For example, if you have about 5GB data growing yearly, you want to split it to small fs files
	#	so your http users could download small packs of specific data they want to monitor without overloading 
	#	server too much on every fs open file. Every object is a separate .fs file(actually 4 files which grows 1Kb per update)
	def __init__(self, objects, prefix = 'bf', exclude = '[$]'):
		self._timer = str(int(time.time()))
		self._counter = len(objects.items())
		self._objects = objects
		self._prefix = prefix
		self._exclude = exclude
	
	#	update data structure with timestamp
	def UpdateObjects(self):
		for pair in self._objects:
			tmpkey = re.sub(self._exclude, '', pair)		#	remove forbidden symbols from the key
			bfname = self._prefix + tmpkey				#	forming unique buffer name
			self.InitDB(bfname)					#	open ZDOB collection
			self.root[self._timer] = self._objects[pair]		#	the actual writing of the data to the corresponding file
			self.CloseDB()						#	close ZDOB connection and commit transaction
			#print("{} : {}".format(pair, self._objects[pair]))
		print("Counter:{}".format(self._counter))
	
	
	def GetCollectionBySymbol(self, symbol):
		self.InitDB(self._prefix + symbol)
		print(symbol)
		for col in self.root:
			print("\t{}:\n\t\t{}".format(col, self.root[col]))
	
	
	def InitDB(self, fname):
		#	create storage from compressed data
		self.storage = zc.bz2storage.Bz2Storage(FileStorage.FileStorage(fname+'.fs'))
		#print(self.storage)
		#	create DB that uses our storage
		self.db = DB(self.storage)
		#	open DB connection object
		self.connection = self.db.open()
		#	get the root access
		self.root = self.connection.root()
	
	#	split objects into chunks of defined size
	def chunks(self, data, SIZE=100):
		it = iter(data)
		for i in range(0, len(data), SIZE):
			yield {k:data[k] for k in islice(it, SIZE)}
	
	
	def CloseDB(self):
		transaction.commit()
		#print(self.root.items())
		self.connection.close()
		self.db.close()
		self.storage.close()
	
	
	def DropTables(self, folder = '/home/ubuntu/folder/'):
		for pair in self._objects:
			tmpkey = re.sub(self._exclude, '', pair)		#	remove forbidden symbols from the key
			bfname = self._prefix + tmpkey				#	forming unique buffer name
			os.system('rm -rf '+ folder + bfname+'.*')
