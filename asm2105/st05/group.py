
class Group:
    def __init__(self, strategy, storage, count = 0):
        self.group_members = []
        self.strategy = strategy
        self.storage = storage()


    def add(self, dino):
        #for elem in self.group_members:
         #   if elem.id<len(self.group_members):
          #      dino.id = len(self.group_members)+1
           # else: dino.id = len(self.group_members)
        #dino.id = len(self.group_members)
        if (len(self.group_members) != 0):
            lastId = self.group_members[len(self.group_members)-1].id
        else: lastId = -1
        dino.id = lastId+1

        dino.set()
        self.group_members.append(dino)

    def show(self):
        for dino in self.group_members:
            dino.get()

    def load(self):
        self.group_members = self.storage.load()

    def save(self):
        self.storage.save(self.group_members)

    def clear(self):
        self.group_members.clear()

    def deleteObject(self,n):
        i=-1
        for elem in self.group_members:
            i+=1
            if elem.id==int(n):
                self.group_members.pop(i)
                break

         #   else: dino.id = len(self.group_members)


        #if(len(self.group_members)!=0):
         #   if(len(self.group_members)>int(n)):
          #      self.group_members.pop(int(n))

#        id = -1
 #       for dino in self.group_members:
  #          id+=1
   #         dino.id=id

