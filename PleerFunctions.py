import urllib
import urllib.parse
import urllib.request as urllib2
import json


def parse_tracks(html):
	""" Parse HTML to retrieve listed tracks """
	records = json.loads(html.decode('utf8'))
	matches = []
	
	for item in records['tracks'] :
		details = {
			'artist': item['artist'], 
			'song': item['track'], 
			'duration': item['length'], 
			'link': item['file']
		}
		matches.append(details)
	
	return(matches)

