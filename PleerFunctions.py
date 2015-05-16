import urllib
import urllib.parse
import urllib.request as urllib2
import json

import re


def parse_tracks(html):
	""" Parse HTML to retrieve listed tracks """
	records = json.loads(html.decode('utf8'))
	matches = []
	
	for item in records['tracks'] :
#		print records
		details = {
			'artist': item['artist'], 
			'song': item['track'], 
			'duration': item['length'], 
			'link': item['id']
		}
		matches.append(details)
	
	return(matches)


def getMp3URL(linkId):
	""" Query Pleer API to get MP3 URL for given id"""
	
	url = 'http://pleer.com/browser-extension/files/%s.mp3' % linkId
	
	return(url)

