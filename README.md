
# KNN Clssifier
Implemented a KNN classifier to predict people's income.  

## Data Description
Data set:  
Traning data: income_tr.csv  
Test dara: income_te.csv  

Features:  
age    
workclass	
fnlwgt	
education	
education_cat	
marital_status	
occupation	
relationship	
race    	
gender	
capital_gain	
capital_loss	
hour_per_week	
native_country

##Data Preprocessing  
* Use Min Max approach to normalize the data
* How to cope with categorical features: 
    * the proximity/similarity is 1 if two records have the same value for that feature , otherwise 0

## Computing Proximity/ Similarity
Euclidean distance and Cosine similarity   



## Performance  
### Euclidean distance

Accuracy for 80% for k=25

### Cosine Similarity
Accuracy for 77% for k=7
