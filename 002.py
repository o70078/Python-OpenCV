#coding=utf-8
class pyc(object):

    def __init__(self,NumA):
        self.NumA=NumA

    def GetNumA(self):
        return self.NumA

if __name__ == "__main__":
    pppp=pyc(12)
    print "NumA =",pppp.GetNumA()
    arr=[1,2,3,4]
    #把arr每个元素+1 然后给arrb
    arrb=[x+1 for x in arr]
    arrc=[x for x in arr if i>2]
    print arrc