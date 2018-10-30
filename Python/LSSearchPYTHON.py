def linearSearch(ls,data):

   for item in ls:
       if item == data:
           return True
   return False

print(linearSearch([6,3,9,0,5,8,2],0))
