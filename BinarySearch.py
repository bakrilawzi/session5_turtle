class binarySearch:

    def __init__(self,listt,secNum):
        self.listt = listt
        self.secNum  = secNum

    def search_inside(self):
        head = 0
        last = len(self.listt)-1
        print("the last item",last)
        while head<=last:
            midpoint = round((head+last)/2)
            print(("the midpoint is : ",midpoint))
            if self.listt[midpoint] == self.secNum:
                head =  last+1
                return midpoint
            elif self.listt[midpoint]>self.secNum:
                last = midpoint-1
                print("the new last",last)
            else:
                head = midpoint+1
                print("the new head",head)
        return None
    def verify(self,index):
         if index is not None:
             print(f"targer is on the {index} index")
         else:
             print("the target doesn't exist")