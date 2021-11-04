def description_from_url_walmart(link):
	description = ''
	try:
		remove_initial = link.replace("https://www.walmart.com/ip/","")
		for i in remove_initial:
			if(i!="/"):
				description += i
			else:
				break
		description  = description.replace('-',' ')
	except:
		description = ''
	return description


