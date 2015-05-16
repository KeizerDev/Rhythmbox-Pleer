import rb
import urllib.request as urllib2
import hashlib
import codecs

from xml.dom import minidom
from gi.repository import RB

from PleerResult import PleerResult

import PleerFunctions

class PleerSearch:
	def __init__(self, search_term, db, entry_type):
		self.search_term = search_term
		self.db = db
		self.entry_type = entry_type
		self.search_complete = False
		self.entries_hashes = []
		self.query_model = RB.RhythmDBQueryModel.new_empty(db)

	def is_complete(self):
		return self.search_complete

	def add_entry(self, result):
		entry = self.db.entry_lookup_by_location(result.url)
		
		self.entries_hashes.append(hash)
		
		if entry is None:
			entry = RB.RhythmDBEntry.new(self.db, self.entry_type, result.url)
			if result.title:
				self.db.entry_set(entry, RB.RhythmDBPropType.TITLE, result.title)
			if result.duration:
				self.db.entry_set(entry, RB.RhythmDBPropType.DURATION, result.duration)
			if result.artist:
				self.db.entry_set(entry, RB.RhythmDBPropType.ARTIST, result.artist)
		self.query_model.add_entry(entry, -1)
		self.db.commit()

	# Called when HTTP request is done (See start() method)
	def on_search_results_recieved(self, data):
		# Parse and fetch songs list
		tracks = PleerFunctions.parse_tracks(data)
		
		for currTrack in tracks:
			self.add_entry(PleerResult(currTrack))
		
		self.search_complete = True

	# Button "Search button" callback function
	def start(self):
		path = 'http://pleer.com/browser-extension/search?q='+ self.search_term
		loader = rb.Loader()
		loader.get_url(path, self.on_search_results_recieved)

