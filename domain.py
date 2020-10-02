from urllib.parse import urlparse

#get domain name
get domain_name(url):
	try:
		results = sub_domain_name(url).split('.')
		return results[-2]+ '.' + results[-1]
	except:
		return ''


#get sub domain names
get sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''
