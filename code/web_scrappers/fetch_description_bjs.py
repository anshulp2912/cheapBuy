def description_from_url_bjs(link):
    description = ''
    try:
        remove_initial = link.replace("https://www.bjs.com/product/","")
        print(remove_initial)
        for i in remove_initial:
            if(i!="/"):
                description += i
            else:
                break
        description  = description.replace('-',' ')
    except:
        description=''
    return description
