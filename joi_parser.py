from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def get_url(page="/363"):
	try:
		url = 'http://anime.reactor.cc/tag/Asuka+Langley'+page
		html = urlopen(url)
	except HTTPError as e:
		print (e)
	else:
		bsObj = BeautifulSoup(html.read(), features="html.parser")
		res = []
		#print (bsObj.findAll(text = re.compile('prettyPhotoLink')))
		for n in bsObj.findAll('a',{'class':'prettyPhotoLink'}):
			res.append(re.sub(r'full/', '', n['href']))
		return res

