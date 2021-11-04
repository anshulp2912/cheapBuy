def description_from_url_costco(link):
	description = ''
	try:
		remove_initial = link.replace("https://www.costco.com/","")
		for i in remove_initial:
			if(i!="."):
				description += i
			else:
				break
		description  = description.replace('-',' ')
	except:
		description = ''
	return description
