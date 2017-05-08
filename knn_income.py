import sys, csv, operator, math
#from income import euclidean

def loadData(file, data=[]):
	min1= dict()
	max1= dict()
	min_age= sys.maxint
	max_age= -min_age
	min_fn= sys.maxint
	max_fn= -min_fn
	min_edu_cat= sys.maxint
	max_edu_cat= -min_edu_cat
	min_c_gain= sys.maxint
	max_c_gain= -min_c_gain
	min_c_loss= sys.maxint
	max_c_loss= -min_c_loss
	min_hours= sys.maxint
	max_hours= -min_hours

	with open (file) as csvfile:
		i= 0
		for line in csvfile:
			#print line
			content= [item.strip() for item in line.replace('"','').split(',')]
			i+= 1
			if i==1:
				continue
			
			#print len(content)
			new_row= dict()
			new_row['ID']= int(content[0])
			new_row['age']= int(content[1])
			if int(new_row['age'])< min_age:
				min_age= int(new_row['age'])
			if int(max_age)< int (new_row['age']):
				max_age= int(new_row['age'])
			new_row['workclass']= content[2]
			new_row['fn']= int(content[3])
			if max_fn< int(new_row['fn']):
				max_fn= int(new_row['fn'])
			if min_fn> int(new_row['fn']):
				min_fn= int(new_row['fn'])
			new_row['education']= content[4]
			new_row['edu_cat']= int(content[5])
			if max_edu_cat< int(new_row['edu_cat']):
				max_edu_cat= int(new_row['edu_cat'])
			if min_edu_cat> int(new_row['edu_cat']):
				min_edu_cat= int(new_row['edu_cat'])
			new_row['marital']= content[6]
			new_row['occupation']= content[7]
			new_row['relationship']= content[8]
			new_row['race']= content[9]
			new_row['gender']= content[10]
			new_row['capital_gain']= int(content[11])
			if max_c_gain< int(new_row['capital_gain']):
				max_c_gain= int(new_row['capital_gain'])
			if min_c_gain> int(new_row['capital_gain']):
				min_c_gain= int(new_row['capital_gain'])
			new_row['capital_loss']= int(content[12])
			if max_c_loss< int(new_row['capital_loss']):
				max_c_loss= int(new_row['capital_loss'])
			if min_c_loss> int(new_row['capital_loss']):
				min_c_loss= int(new_row['capital_loss'])
			new_row['hours']= int(content[13])
			if max_hours< int(new_row['hours']):
				max_hours= int(new_row['hours'])
			if min_hours> int(new_row['hours']):
				min_hours= int(new_row['hours'])
			new_row['country']= content[14]
			new_row['class']= content[15]
			#print "new_row" , new_row
			data.append(new_row)
		min1['age']= min_age
			#print "age= ", min['age'], min_age
		min1['fn']= min_fn
		min1['edu_cat']= min_edu_cat
		min1['capital_gain']= min_c_gain
		min1['capital_loss']= min_c_loss
		min1['hours']= min_hours
		max1['age']= max_age
		max1['fn']= max_fn
		max1['edu_cat']= max_edu_cat
		max1['capital_gain']= max_c_gain
		max1['capital_loss']= max_c_loss
		max1['hours']= max_hours
		result= []
		result.append(min1)
		result.append(max1)
	return result

def cosineSimilar(r1, r2, min_v, max_v):

	if len(r1)!= len(r2):
		print "the length is not compatible"
		return
	"""
	len1= math,sqrt(r1['age']* r1['age']+ r1['fn']* r1['fn']+ r1['edu_cat']* r1['edu_cat']+ r1['capital_gain']* r1['capital_gain']+\
		 r1['capital_loss']* r1['capital_loss']+ r1['hours']* r1['hours'])

	len2= math.sqrt(r2['age']* r2['age']+ r2['fn']* r2['fn']+ r2['edu_cat']* r2['edu_cat']+ r2['capital_gain']* r2['capital_gain']+\
		 r2['capital_loss']* r2['capital_loss']+ r2['hours']* r2['hours'])
	"""
	r3=dict()
	r4=dict()
	r3['age']= (float(r1['age'])- float(min_v['age']))/(float(max_v['age'])- float(min_v['age']))
	#print "r3['age']= ", r3['age']
	r4['age']= (float(r2['age'])- float (min_v['age']) )/(float(max_v['age'])- float(min_v['age']))
	r3['fn']= (float(r1['fn'])- float(min_v['fn']))/(float(max_v['fn'])- float(min_v['fn']) )
	r4['fn']= (float (r2['fn'])- float(min_v['fn'])) /(float(max_v['fn'])- float(min_v['fn']) )
	r3['edu_cat']= (float (r1['edu_cat'])- float(min_v['edu_cat']))/(float (max_v['edu_cat'])- float(min_v['edu_cat']))
	r4['edu_cat']= (float (r2['edu_cat'])- float(min_v['edu_cat']))/(float(max_v['edu_cat'])- float(min_v['edu_cat']))
	r3['capital_gain']= (float (r1['capital_gain'])- float(min_v['capital_gain']))/ (float(max_v['capital_gain'])- float(min_v['capital_gain']))
	r4['capital_gain']= (float (r2['capital_gain'])- float(min_v['capital_gain']))/ (float(max_v['capital_gain'])- float(min_v['capital_gain']))
	r3['capital_loss']= (float(r1['capital_loss'])- float(min_v['capital_loss']))/ (float(max_v['capital_loss'])- float(min_v['capital_loss']))
	r4['capital_loss']= (float(r2['capital_loss'])- float(min_v['capital_loss']))/ (float(max_v['capital_loss'])- float(min_v['capital_loss']))
	r3['hours']= (float(r1['hours'])- float(min_v['hours']))/ (float(max_v['hours'])- float(min_v['hours']))
	r4['hours']= (float(r2['hours'])- float(min_v['hours']))/ (float(max_v['hours'])- float(min_v['hours']))
	p= product(r3, r4)
	#print "product", product(r4, r4)
	len1= math.sqrt(product(r3, r3))
	len2= math.sqrt(product(r4, r4))


	similar=0
	if r1['workclass']== r2['workclass']:
		similar+=1
	if r1['marital']== r2['marital']:
		similar+=1
	if r1['occupation']== r2['occupation']:
		similar+=1
	if r1['relationship']== r2['relationship']:
		similar+=1
	if r1['race']== r2['race']:
		similar+=1
	if r1['gender']== r2['gender']:
		similar+=1
	if r1['country']== r2['country']:
		similar+=1
	#if r1['education']== r2['education']:
		#similar+=1
	#print float(p)/ (1.0* (len1* len2))
	#print float(similar)/8.0
	#print "p=", p, "len1=", len1, "len2= ", len2, "similar= ", similar
	#print "cosine similarity", float(p)/ (1.0* (len1* len2))+ float(similar)/7.0
	return float(p)/ (1.0* (len1* len2))+ float(similar)/7.0

def product(r1, r2):
	if r1['age']< r1['fn']<0 or r1['edu_cat']<0 or r1['capital_gain']<0 or r1['capital_loss']<0 or r1['hours']<0:
		print r1, "has negative valuessssssss"
		#return
	product= float(r1['age'])* float(r2['age'])+ float(r1['fn'])* float(r2['fn'])+ float(r1['edu_cat'])* float(r2['edu_cat'])+ float(r1['capital_gain'])* float(r2['capital_gain'])+\
		 float(r1['capital_loss'])* float(r2['capital_loss'])+ float(r1['hours'])* float(r2['hours'])
	return product

def euclidean(r1, r2, min_v, max_v):
	age= ((float(r1['age'])- float(r2['age']))/ (float(max_v['age']- min_v['age'])) )* ((float(r1['age'])- float(r2['age']))/ (float(max_v['age'])- float(min_v['age'])))
	fn= ((float(r1['fn'])- float(r2['fn']))/ (float(max_v['fn'])- float(min_v['fn']))) * ((float(r1['fn'])- float(r2['fn']))/ (float(max_v['fn'])-float(min_v['fn']) ))
	edu_cat= ((float(r1['edu_cat'])- float(r2['edu_cat']))/ (float(max_v['edu_cat'])- float(min_v['edu_cat']))) * ((float(r1['edu_cat'])- float(r2['edu_cat']))/ (float(max_v['edu_cat'])- float(min_v['edu_cat'])))
	capital_gain= ((float(r1['capital_gain'])- float(r2['capital_gain']))/ (float(max_v['capital_gain'])- float(min_v['capital_gain']) )) \
	* ((float(r1['capital_gain'])- float(r2['capital_gain']))/ (float(max_v['capital_gain'])- float(min_v['capital_gain'])))
	capital_loss= ((float(r1['capital_loss'])- float(r2['capital_loss']))/ (float(max_v['capital_loss'])- float(min_v['capital_loss'])))\
	 * ((float(r1['capital_loss'])- float(r2['capital_loss']))/ (float(max_v['capital_loss'])-float(min_v['capital_loss']) ))
	hours= ((float(r1['hours'])- float(r2['hours']))/ (float(max_v['hours'])- float(min_v['hours']))) * ((float(r1['hours'])- float(r2['hours']))/ (float(max_v['hours'])- float(min_v['hours'])))
	dis= 0
	if r1['workclass']!= r2['workclass']:
		dis+=1
	if r1['marital']!= r2['marital']:
		dis+=1
	if r1['occupation']!= r2['occupation']:
		dis+=1
	if r1['relationship']!= r2['relationship']:
		dis+=1
	if r1['race']!= r2['race']:
		dis+=1
	if r1['gender']!= r2['gender']:
		dis+=1
	if r1['country']!= r2['country']:
		dis+=1

	return math.sqrt(age+fn+edu_cat+capital_gain+capital_loss+hours+ float(dis)/7.0)

#def compareMax(max1, max2):
def getNeighbors(testInstance, trainging_set, min_v, max_v, k, approach):
	result1=[]
	for i in range(len(trainging_set)):
		if approach=="E":
			proximity= euclidean(testInstance, trainging_set[i], min_v, max_v)
		elif approach=="C":
			proximity= cosineSimilar(testInstance, trainging_set[i], min_v, max_v)
		else:
			print "Invalid approach"
			return
		item= dict()
		item['id']= trainging_set[i]['ID']
		item['proximity']= proximity
		item['class']= trainging_set[i]['class']
		result1.append(item)
	if approach=="E":
		result1= sorted(result1, key= lambda k: k['proximity'])
	elif approach=="C":
		result1= sorted(result1, key= lambda k: k['proximity'], reverse= True)

	neighbors=[]
	for j in range(k):
		neighbors.append(result1[j])
	return neighbors

def getClass(neighbors):
	classVotes={}
	#print "neighbors:", neighbors
	for x in range(len(neighbors)):
		
		vote= neighbors[x]['class']
		if vote in classVotes:
			classVotes[vote]+=1
		else:
			classVotes[vote]= 1
	#print "class voteee", classVotes
	sortedVote= sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	#print "sorted vote",sortedVote
	#print "postterior= ", sortedVote[0][1]
	return sortedVote[0]

def getAccuracy(testInstace, predict):
	correct= 0

	if testInstace['class']== predict:
		correct+=1
	return correct

def title():
	print "Transaction ID  Actual class  Predicted Class  Posterior"

def ROC(neighbors, k):
	classVotes={}
	for x in range(len(neighbors)):
		vote= neighbors[x]['class']
		if vote in classVotes:
			classVotes[vote]+= 1.0/float(k)
		else:
			classVotes[vote]= 1/float(k)
	#print "classVote", classVotes
	pos= "<=50K"
	if pos in classVotes:
		#print classVotes[pos]
		return classVotes[pos]
	else:
		return 0
	#if classVotes[0][0]

	#for each test record, get the posteriror of being positive
	#sort the postrior above in reverse order
	#pick the threshold
	#TPR= TP/(all the test rcords that are actully postive)
	#FPR= FP/(all the test records that are actually negative)

def confusionMatrix(predictions, actual):
	#confuse[0][0]:<=50, <=50
	#confuse[0][1]: <=50, >50
	
	#confuse[1][0]: >50, <=50
	#confuse[1][1]:>50, >50
	
	confuse= [[0, 0]for i in range(2)]
	for i in range(len(actual)):
		#for j in range(len(predictions)):
			if actual[i]== "<=50K":
				if predictions[i]== "<=50K":
					confuse[0][0]+=1
				elif predictions[i]== ">50K" :
					confuse[0][1]+=1
				
			if actual[i]==">50K":
				if predictions[i]== "<=50K":
					confuse[1][0]+=1
				elif predictions[i]== ">50K" :
					confuse[1][1]+=1
			
	print "Confusion Matrix", confuse

def main():
	if len(sys.argv)< 3:
		print "Input fromat: python knn_income.py k approach"
		return
	approach= sys.argv[2]   
	#approach= "C" Cosine
	#approach= "E"  Euclidean
	k= int(sys.argv[1])
	train= []
	result= loadData("income_tr.csv", train)
	#print "the max and min", result
	test=[]
	loadData("income_te.csv", test)

	correct= 0
	title()
	predictions=[]
	actuals=[]
	totalPos= 0
	for i in range(len(test)):
		#print "test ", i, test[i]
		neighbors= getNeighbors(test[i], train, result[0], result[1], k, approach)
		predict= getClass(neighbors)
		#print predict
		"""
		predict = ROC(neighbors, k)
		if predict> 1:

			predictions.append("<=50K")
		else:

			#print test[i]['class'], predict
			predictions.append(">50K")
		#print "predict for test", i, predict
	
		correct+= getAccuracy(test[i], predictions[0])
		"""
		
		postterior= float(predict[1])/(1.0* k)
		predictions.append(predict[0])
		correct+= getAccuracy(test[i], predict[0])
		actuals.append(test[i]['class'])
		if test[i]['class']== "<=50K":
			totalPos+=1
		#print "nei", neighbors
		print test[i]['ID'], "           ", test[i]['class'], "         ", predict[0], "        ", postterior
	print "correct prediction= ", correct
	acc_rate= float(correct)/ (1.0*len(test))
	print "Accuray rate ", acc_rate, "Error rate ", 1- acc_rate
	confusionMatrix(predictions, actuals)
	#print "total positive= ", totalPos
	#print "result: lala", result[0], result[1]
	#convertData(data, result[0], result[1])
	#getNeighbors(data, 3, result[0], result[1])

main()