import numpy

# The first method
def paging(list_page,page):
	over=[]
	slice=int(len(list_page)/page)
	if slice == len(list_page)/page:
		listNum=numpy.array(list_page)
	else:
		over=list_page[page*slice:]
		listNum=numpy.array(list_page[:page*slice])
	pageList=listNum.reshape(slice,page).tolist()
	pageList.append(over)
	return pageList


# The second method
def segmentation(list,number):
	pages=[list[x:x+number] for x in range(0,len(list),number)]
	return pages

list= [1,2,3,4,5,6,7,8,9,10]
print(paging(list,4))
print(segmentation(list,4))