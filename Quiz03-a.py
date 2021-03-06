def dot(vector01,vector02):
  '''
  Inputs
    vector01 should be 1 x n in length
    vector02 should be 1 x n in length

  Output should be a scalar

  This function compares the lengths of two vectors together.  
  If they are the same length it multiolies the first column of vector01 by the first column of vector02.
  Next it takes this value and stores it in the out container.  
  it repeats this multiplication for each column and adds the products together inside of the out container.
    '''

  if len(vector01)==len(vector02) and len(vector01)!=0:#checks to see that the two vectors are the same length and the second vector is not 0
    out = 0 # starts the holding array at 0
    for k in range(len(vector01)):
        out += vector01[k] * vector02[k]# for each iteration after the product is done it adds the number into the container out
    return out
  else:
    print("input invalid")
    
#testvec1 = a
#testvec2 = [4,5,6]
#testvec0 = apple

#print(dot(testvec1,testvec2))
