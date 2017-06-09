from numpy import *

a=array(
    [
        [
            [0,1,2],[3,4,5],[10,91,12],[33,41,45]
        ],
        [
            [12,21,1],[13,24,15],[251,222,123],[5,123,66]
        ]
    ]
,dtype=uint8)

b=array(
    [
        [0,1,2],[3,4,5],[10,91,12],[33,41,45]
    ]
,dtype=uint8)

print b
print "----------"
print b[:,1]
print "----------"
print b[1,:]
print "----------"
print [b[x,x] for x in range(3)]
print "----------"
print zip([1,2,3],[4,5,6])

#print b[1,:]*b[:,1]

a[:,:,0]=12
a[:,:,1]=a[:,:,1]*2
a[:,:,2]=arange(8).reshape(2,4)

#print a