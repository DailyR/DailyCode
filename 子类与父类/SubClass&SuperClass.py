#-*- coding:utf-8 -*-  
#Sample_Python.py  
#just used for 
''''' 
Created on 2015-X-XX 
 
@author: daily 
'''
#Sample


def main():
	'''docstring'''
	print "hello world!"

def run():
	ClassSon1(1)

class A(object):# correctly answer  A(object)  wrong A: or A():
    def __init__(self):
        self.namea="aaa"
    def funca(self):
        print "function a : %s"%self.namea

class B(A):
    def __init__(self):
    	#正确的声明，子类和父类的声明
    	super(B,self).__init__()  #试试注销这一行，就会出错噢。
    	#A.__init__(self)   #改成此行声明父类关系也可以，但是复杂父类超类关系的时候就有很多复杂关系会出错，所以一般都用super的方式声明
        self.nameb="bbb"

    def funcb(self):
        
        print "function b : %s"%self.nameb

		
if __name__ == '__main__':
	main()
	b=B()
	print b.nameb
	b.funcb()
	b.funca()