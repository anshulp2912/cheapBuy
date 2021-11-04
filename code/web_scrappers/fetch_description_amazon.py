def description_from_url_amazon(link):
	description = ''
	try:
		link = link.replace('https://www.amazon.com/','')
		for ch in link:
			if ch!='/':
				description+=ch
			else:
				break
		description = description.replace('-', ' ')
	except:
		description = ''
	return description