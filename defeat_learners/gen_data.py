"""  		   	  			    		  		  		    	 		 		   		 		  
template for generating data to fool learners (c) 2016 Tucker Balch  		   	  			    		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		   	  			    		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		   	  			    		  		  		    	 		 		   		 		  
All Rights Reserved  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		   	  			    		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		   	  			    		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		   	  			    		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		   	  			    		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		   	  			    		  		  		    	 		 		   		 		  
or edited.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		   	  			    		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		   	  			    		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		   	  			    		  		  		    	 		 		   		 		  
GT honor code violation.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
  Student Name: ZHENG FU
  GT User ID: zfu66
  GT ID: 903369876 		   	  			    		  		  		    	 		 		   		 		  
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import math  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
# this function should return a dataset (X and Y) that will work  		   	  			    		  		  		    	 		 		   		 		  
# better for linear regression than decision trees  		   	  			    		  		  		    	 		 		   		 		  
def best4LinReg(seed=1489683273):  		   	  			    		  		  		    	 		 		   		 		  
    np.random.seed(seed)  		   	  			    		  		  		    	 		 		   		 		  
    X = np.zeros((100,2))  		   	  			    		  		  		    	 		 		   		 		  		   	  			    		  		  		    	 		 		   		 		  
    # Here's is an example of creating a Y from randomly generated  		   	  			    		  		  		    	 		 		   		 		  
    # X with multiple columns  		   	  			    		  		  		    	 		 		   		 		  
    # Y = X[:,0] + np.sin(X[:,1]) + X[:,2]**2 + X[:,3]**3 
    data1 = np.random.random(size = (100,))*200-100
    data2 = 10 * data1
    X[:,0] = data1
    X[:,1] = data2
    Y = X[:,0] + X[:,1]

    return X, Y  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def best4DT(seed=1489683273):  	
    np.random.seed(seed)  		 
    X = np.random.normal(size = (100, 3))
    Y = np.zeros(100)
    for i in range(100):
      if X[i, 1] <= 0:
        Y[i] = 1
      else:
        Y[i] = 0

    return X, Y  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def author():  		   	  			    		  		  		    	 		 		   		 		  
    return 'zfu66' #Change this to your user ID  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "Freedom!"  		   
    #X1, Y1 = best4DT(seed=1489683273)			  
    #X1, Y1 = best4LinReg(seed=1489683273)   		  		  		    	 		 		   		 		  
