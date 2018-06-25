
4#A.H.V Darshana

class Queue: 
    def __init__(self): 
        self.items = [] 

    def isEmpty(self): 
        return len(self.items) == 0 

    def enqueue(self, item): 
        self.items.insert(0,item) 
 
    def dequeue(self): 
        return self.items.pop() 
 
    def size(self): 
        return len(self.items)
    
    def show(self):
        print (self.items)


wait_list=[]
carpark=Queue()

print ("=============== CAR PARK ================")
class Car:
    def __init__(self,carNo):
        self.numPL=carNo



    def A(self):#A=Arrive
        if carpark.size()<10 and len(wait_list)==0:
            carpark.enqueue(self.numPL)
            
            
            print ("________________")
            print ("No:{0} Car Added To THE CAR PARK. ".format(self.numPL))

            


        elif carpark.size()<10 and len(wait_list)!=0:
            b=wait_list.pop(0)
            carpark.enqueue(b)
            print ("NO:{0} waited car added to Car park.".format(b))

        else:
            wait_list.append(self.numPL)
            print ("==========Waiting List==========")
            print ("NO:{0} car is in the waiting List.".format(self.numPL))
        
    def D(self):#Derive
        stp=[]
        
        for i in range(0,carpark.size()):
            a=carpark.dequeue()
            
            if self.numPL!=a:
                
                stp.insert(0,a)
        else:
            print ("-----------------------------------------------")
            print ("NO:{0} car has Derrived.There're space here".format(self.numPL))

                
        for j in range(0,len(stp)):
            carpark.enqueue(stp.pop())

        if carpark.size()<10 and len(wait_list)!=0:
            carpark.enqueue(wait_list[0])
            print ("No:{0} car Added To THE CAR PARK.".format(wait_list[0]) )
            del wait_list[0]

#A=Arrive car
#D=Arrive car
        
c1=Car('001-2055')
c1.A()
c2=Car('052-4143')
c2.A()
c3=Car('350-5121')
c3.A()
c4=Car('41-2541')
c4.A()
c5=Car('55-8754')
c5.A()
c6=Car('6588-754')
c6.A()
c7=Car('7857-5845')
c7.A()
c8=Car('85-4587-21')
c8.A()
c9=Car('974-15842')
c9.A()
c10=Car('241-2543')
c10.A()
c11=Car('1158-2155')
c11.A()
c12=Car('1748-8745')
c12.A()
#Derrieved car
c8.D()
c5.D()

c1.D()

c13=Car("1025-4875")
c13.A()
carpark.show()

