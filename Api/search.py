from Ecom.models import Product

def searchAdv(keyword):
	query_set ;
	list5th = ['5','5 TH','5 th', '5 th Standard', '5 th Standard', '5 th Std', '5 th Standard''5 th Standrad', '5 th Standrad', '5 th Std', '5 th Standrad','5 th books',
	           '5th books','5 th Std books','5 th Standard books','5 th Books','5th Books','5 th Std Books','5 th Standard Books','5 th book','5th book',
	           '5 th Std book','5 th Standard book','5 th Book','5th Book','5 th Std Book','5 th Standard Book']
	list6th = ['6','6 TH', '6 th Standard', '6 th Standard', '6 th Std', '6 th Standard''6 th Standrad', '6 th Standrad', '6 th Std', '6 th Standrad',
	           '6 th books','6th books','6 th Std books','6 th Standard books','6 th Books','6th Books','6 th Std Books','6 th Standard Books',
	           '6 th book','6th book','6 th Std book','6 th Standard book','6 th Book','6th Book','6 th Std Book','6 th Standard Book']
	list7th = ['7','7 TH', '7 th Standard', '7 th Standard', '7 th Std', '7 th Standard''7 th Standrad', '7 th Standrad', '7 th Std', '7 th Standrad',
	            '7 th books','7th books','7 th Std books','7 th Standard books','7 th Books','7th Books','7 th Std Books','7 th Standard Books',
	            '7 th book','7th book','7 th Std book','7 th Standard book','7 th Book','7th Book','7 th Std Book','7 th Standard Book']
	list8th = ['8','8 TH', '8 th Standard', '8 th Standard', '8 th Std', '8 th Standard''8 th Standrad', '8 th Standrad', '8 th Std', '8 th Standrad',
	        '8 th books','8th books','8 th Std books','8 th Standard books','8 th Books','8th Books','8 th Std Books','8 th Standard Books',
	        '8 th book','8th book','8 th Std book','8 th Standard book','8 th Book','8th Book','8 th Std Book','8 th Standard Book']

	list9th = ['9', '9 th', '9 TH', '9 th Standard', '9 th Standard', '9 th Std', '9 th Standard''9 th Standrad', '9 th Standrad', '9 th Std',
	           '9 th Standrad','9 th books','9th books','9 th Std books','9 th Standard books','9 th Books','9th Books','9 th Std Books',
	           '9 th Standard Books','9 th book','9th book','9 th Std book','9 th Standard book','9 th Book','9th Book','9 th Std Book','9 th Standard Book']
	list10th = ['10','10 TH', '10 th Standard', '10 th Standard', '10 th Std', '10 th Standard''10 th Standrad', '10 th Standrad', '10 th Std', 
	            '10 th Standrad','10 th books','10th books','10 th Std books','10 th Standard books','10 th Books','10th Books','10 th Std Books',
	            '10 th Standard Books','10 th book','10th book','10 th Std book','10 th Standard book','10 th Book','10th Book','10 th Std Book',
	            '10 th Standard Book']

	list11th = ['11','11 TH', '11 th Standard', '11 th Standard', '11 th Std', '11 th Standard''11 th Standrad', '11 th Standrad', '11 th Std', 
	            '11 th Standrad','11 th books','11th books','11 th Std books','11 th Standard books','11 th Books','11th Books','11 th Std Books',
	            '11 th Standard Books','11 th book','11th book','11 th Std book','11 th Standard book','11 th Book','11th Book','11 th Std Book',
	            '11 th Standard Book']

	list12th = ['12','12 TH', '12 th Standard', '12 th Standard', '12 th Std', '12 th Standard''12 th Standrad', '12 th Standrad', '12 th Std', 
	            '12 th Standrad','12 th books','12th books','12 th Std books','12 th Standard books','12 th Books','12th Books','12 th Std Books',
	            '12 th Standard Books','12 th book','12th book','12 th Std book','12 th Standard book','12 th Book','12th Book','12 th Std Book',
	            '12 th Standard Book']



	branch1 = [' Science',' science',' SCI',' SCIENCE',' Sci',' Sci.',' SCI.']
	branch2 = [' ARTS',' arts',' Arts',' art',' Art',' ART',' arts.',' ARTS.']
	branch3 = [' Commerce',' COMMERCE',' commerce',' Com',' Com.',' COM',' COM.',' com.',' com']
	Catlist = [' Textbook',' Textbooks',' TB',' tb',' text book',' textbook',' Text Book']
	Catlist1 = [' Digest','DIGEST',' Digests','DIGESTS',' DIG' ,' Dig','Digst','Digest']
	#Catlist2 = ['HH','hh','Helping Hands','HELPING HANDS','HELPING','helping','helping Hands''helping hands''helping Hand''helping hand']
	list5th1 = [] 
	list6th1 = []
	list7th1 = []
	list8th1 = []
	list9th1 = []
	list9th1 = []
	list10th1 = []
	list11thSci1 = []
	list12thSci1 = []
	list11thCom1 = []
	list12thCom1 = []
	list11thArt1 = []
	list12thArt1 = []
	list11thSci2 = []
	list12thSci2 = []
	list11thCom2 = []
	list12thCom2 = []
	list11thArt2 = []
	list12thArt2 = []



	for i in range(0, len(list5th)):
	    for j in range(0 ,len(Catlist)):
	        list5th1.append(list5th[i]+Catlist[j])
	        
	for i in range(0, len(list6th)):
	    for j in range(0 ,len(Catlist)):
	        list6th1.append(list6th[i]+Catlist[j])
	        
	for i in range(0, len(list7th)):
	    for j in range(0 ,len(Catlist)):
	        list7th1.append(list7th[i]+Catlist[j])
	        
	for i in range(0, len(list8th)):
	    for j in range(0 ,len(Catlist)):
	        list8th1.append(list8th[i]+Catlist[j])
	        
	for i in range(0, len(list9th)):
	    for j in range(0 ,len(Catlist)):
	        list9th1.append(list9th[i]+Catlist[j])
	        
	for i in range(0, len(list10th)):
	    for j in range(0 ,len(Catlist)):
	        list10th1.append(list10th[i]+Catlist[j])

	for i in range(0, len(list11th)):

	    for j in range(0 ,len(Catlist)):
	        list10th1.append(list10th[i]+Catlist[j])

	for i in range(0, len(list11th)):
	    for a in range(0 ,len(branch1)):
	        list11thSci1.append(list11th[i]+branch1[a])
	        list11thSci2.append(list11th[i]+branch1[a])
	    for b in range(0 ,len(branch2)):
	        list11thCom1.append(list11th[i]+branch3[b])
	        list11thCom2.append(list11th[i]+branch3[b])
	    for c in range(0 ,len(branch2)):
	        list11thArt1.append(list11th[i]+branch2[c])
	        list11thArt2.append(list11th[i]+branch2[c])
	    for j in range(0 ,len(Catlist)):
	        list11thSci1.append(list11thSci1[i]+Catlist[j])
	        list11thCom1.append(list11thCom1[i]+Catlist[j])
	        list11thArt1.append(list11thArt1[i]+Catlist[j])

	for i in range(0, len(list12th)):
	    for a in range(0 ,len(branch1)):
	        list12thSci1.append(list12th[i]+branch1[a])
	        list12thSci2.append(list12th[i]+branch1[a])
	    for b in range(0 ,len(branch2)):
	        list12thCom1.append(list12th[i]+branch3[b])
	        list12thCom2.append(list12th[i]+branch3[b])
	    for c in range(0 ,len(branch2)):
	        list12thArt1.append(list12th[i]+branch2[c])
	        list12thArt2.append(list12th[i]+branch2[c])
	    for j in range(0 ,len(Catlist)):
	        list12thSci1.append(list12thSci1[i]+Catlist[j])
	        list12thCom1.append(list12thCom1[i]+Catlist[j])
	        list12thArt1.append(list12thArt1[i]+Catlist[j])

	        
	# print(list5th1)
	# print("***********")
	# print(list6th1)
	# print("***********")
	# print(list7th1)
	# print("***********")
	# print(list8th1)
	# print("***********")
	# print(list9th1)
	# print("***********")
	# print(list10th1)
	# print("***********")
	# print(list11thSci1)
	# print("***********")
	# print(list11thCom1)
	# print("***********")
	# print(list11thArt1)
	# print("***********")
	# print(list12thSci1)
	# print("***********")
	# print(list12thCom1)
	# print("***********")
	# print(list12thArt1)
	# print("***********")
	# print("***********")
	# print(list11thSci2)
	# print("***********")
	# print(list11thCom2)
	# print("***********")
	# print(list11thArt2)
	# print("***********")
	# print(list12thSci2)
	# print("***********")
	# print(list12thCom2)
	# print("***********")
	# print(list12thArt2)
	# print("***********")

	# test_list1 = ['9', '9 th', '9 TH', '9 th Standard', '9 th Standard', '9 th Std', '9 th Standard']
	  
	keyword  = '5 Textbook'
	  
	# res = list(filter(lambda x: list8th in x, keyword))
	res5 = list(filter(lambda x:keyword in x, list5th))
	cat5 = list(filter(lambda x:keyword in x, list5th1))
	res6 = list(filter(lambda x:keyword in x, list6th))
	cat6 = list(filter(lambda x:keyword in x, list6th1))
	res7 = list(filter(lambda x:keyword in x, list7th))
	cat7 = list(filter(lambda x:keyword in x, list7th1))
	res8 = list(filter(lambda x:keyword in x, list8th))
	cat8 = list(filter(lambda x:keyword in x, list8th1))
	res9 = list(filter(lambda x:keyword in x, list9th))
	cat9 = list(filter(lambda x:keyword in x, list9th1))
	res10 = list(filter(lambda x:keyword in x, list10th))
	cat10 = list(filter(lambda x:keyword in x, list10th1))


	res11 = list(filter(lambda x:keyword in x,list11th))
	res11Sci = list(filter(lambda x:keyword in x,list11thSci2))
	res11Com = list(filter(lambda x:keyword in x,list11thCom2))
	res11Art = list(filter(lambda x:keyword in x,list11thArt2))
	cat11Sci1 = list(filter(lambda x:keyword in x,list11thSci1))
	cat11Com1 = list(filter(lambda x:keyword in x,list11thCom1))
	cat11Art1 = list(filter(lambda x:keyword in x,list11thArt1))

	res12 = list(filter(lambda x:keyword in x,list12th))
	res12Sci = list(filter(lambda x:keyword in x,list12thSci2))
	res12Com = list(filter(lambda x:keyword in x,list12thCom2))
	res12Art = list(filter(lambda x:keyword in x,list12thArt2))
	cat12Sci1 = list(filter(lambda x:keyword in x,list12thSci1))
	cat12Com1 = list(filter(lambda x:keyword in x,list12thCom1))
	cat12Art1 = list(filter(lambda x:keyword in x,list12thArt1))

	# res11 = list(filter(lambda x:keyword in x,list12th))
	# res11Sci = list(filter(lambda x:keyword in x, list5th))
	# cat11 = list(filter(lambda x:keyword in x, list5th1))
	# res11 = list(filter(lambda x:keyword in x, list5th))
	# cat11 = list(filter(lambda x:keyword in x, list5th1))
	# res11 = list(filter(lambda x:keyword in x, list5th))
	# cat11 = list(filter(lambda x:keyword in x, list5th1))

	if res5:
	    print("5 th books")
	    query_set = Product.objects.filter(Category=11,medium="English")
	elif cat5:
	    print("5 th textbooks")
	    query_set = Product.objects.filter(Category=11,subCategory=1,medium="English")
	elif res6:
	    print("6 th books")
	    query_set = Product.objects.filter(Category=12,medium="English")
	elif cat6:
	    print("6 th textbooks")
	    query_set = Product.objects.filter(Category=12,subCategory=1,medium="English")
	elif res7:
	    print("7 th books")
	    query_set = Product.objects.filter(Category=13,medium="English")
	elif cat7:
	    print("7 th textbooks")
	    query_set = Product.objects.filter(Category=13,subCategory=1,medium="English")
	elif res8:
	    print("8 th books")
	    query_set = Product.objects.filter(Category=1,medium="English")
	   
	elif cat8:
	    print("8 th textbooks")
	    query_set = Product.objects.filter(Category=1,subCategory=1,medium="English")
	elif res9:
	    query_set = Product.objects.filter(Category=2,medium="English")
	    print("9 th books")
	elif cat9:
	    print("9 th textbooks")
	    query_set = Product.objects.filter(Category=2,subCategory=1,medium="English")
	elif res10:
	    print("10 th books")
	    query_set = Product.objects.filter(Category=5,medium="English")
	elif cat10:
	    print("10 th textbooks")
	    query_set = Product.objects.filter(Category=5,subCategory=1,medium="English")
	elif res11:
	    print("11 th books")
	    query_set = Product.objects.filter(Category=3)
	elif res11Sci:
	    print("11 th Sci books")
	    query_set = Product.objects.filter(Category=3,medium="Science")
	elif res11Com:
	    print("11 th Com books")
	    query_set = Product.objects.filter(Category=3,medium="Commerce")
	elif res11Art:
	    print("11 th Art books")
	    query_set = Product.objects.filter(Category=3,medium="Arts")
	elif cat11Sci1:
	    print("11 th Science textbooks")
	    query_set = Product.objects.filter(Category=3,subCategory=1,medium="Science")
	elif cat11Com1:
	    print("11 th Commerce textbooks")
	    query_set = Product.objects.filter(Category=3,subCategory=1,medium="Commerce")
	elif cat11Art1:
	    print("11 th Artstextbooks")
	    query_set = Product.objects.filter(Category=3,subCategory=1,medium="Arts")
	elif res12:
	    print("12 th books")
	    query_set = Product.objects.filter(Category=4)
	elif res12Sci:
	    print("12 th Sci books")
	    query_set = Product.objects.filter(Category=4,medium="Science")
	elif res12Com:
	    print("12 th Com books")
	    query_set = Product.objects.filter(Category=4,medium="Commerce")
	elif res12Art:
	    print("12 th Art books")
	    query_set = Product.objects.filter(Category=4,medium="Arts")
	elif cat12Sci1:
	    print("12 th Science textbooks")
	    query_set = Product.objects.filter(Category=4,subCategory=1,medium="Science")
	elif cat12Com1:
	    print("12 th Commerce textbooks")
	    query_set = Product.objects.filter(Category=4,subCategory=1,medium="Commerce")
	elif cat12Art1:
	    print("12 th Artstextbooks")
	    query_set = Product.objects.filter(Category=4,subCategory=1,medium="Arts")
	if query_set.exists():
            serializer_object = ProductSerializer(query_set, many=True)
	else :
        query_set = Product.objects.filter(Q(title__icontains=keyword) | Q(medium__icontains=keyword) | Q(slug__icontains=keyword) | Q(desp__icontains=keyword) )
        if query_set.exists():
            serializer_object = ProductSerializer(query_set, many=True)
        else :
            query_set = Product.objects.filter(Q(desp__icontains=keyword))
            serializer_object = ProductSerializer(query_set, many=True)
    return Response(serializer_object.data)
