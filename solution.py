thing = ["l",'i','t','t','l','e','3','4','0']
thing2 = ['r','h','y','n','o','1','2','0','0']

ans2 = ['t','a','l','l','e','r','1','2']
count1 = 0
count2 = 0
ans2 = ['c','r','o','w','d','e','d','2','3']

ans2 = ['m','o','u','s','e','8','3','0']
#ans2 = ['l','i','m','e','s','5','2','0']
#ans2 =['t','h','r','e','a','d','1','5']
#ans2 = ['h','o','u','s','e','4','9','0']

'''
for i in range (len(ans2)):
	if ans2[i] == thing[i]:
		count1 +=1
	if ans2[i] == thing2[i]:
		count2 +=1
'''

thing = ['k','e','y','b','o','a','r','d','9','5','1'] #11
thing2 = ['1','2','3','4','5','d','r','o','n','e','0'] #10

ans2 =['w','o','r','d','e','d','7','3','0','0','0'] #5,7
ans2 = ['5','6','b','r','o','w','n','i','e','0','0'] # 5,9
ans2 =['j','o','h','n','d','r','e','w','9','8','0'] #5,6
ans2 = ['d','r','e','a','m','i','n','g','9','1','0'] #6,6
#ans2 =['b','r','a','n','d','n','e','w','1','2','0'] #6,8
#ans2 = ['c','r','o','w','n','e','d','5','6'] #4,5

for j in range(len(ans2)):
	for i in range (len(ans2)):
		if ans2[j] == thing[i]:
			count1 +=1
		if ans2[j] == thing2[i]:
			count2 +=1

print (count1)
print (count2)