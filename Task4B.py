from timeit import default_timer as timer #importing dafault time from timeit

def selection_sort(list): #function to sort using selection sort algoritthm
    start=timer() #storing starting time
    for i in range (len(list)):
      small=i
      for j in range(i+1,len(list)):
        if list[small]>list[j]:
          small = [j]
          temporary = list[small]
          list[small] = list[i]
          list[i] = temporary
      end=timer() #storing end time
      print("Elapsed time for selection sort :",end-start) #printing elasped time
                

def insertion_sort(list):
  start=timer()

  for i in range(1,len(list)):
    k=list[i]
    h=i-1
    while k<list[h] and h>=0:
      list[h+1]=list[h]
      h=h-1
      list[h+1]=k

    end=timer()
  print("Elapsed time for insertion sort : ", end-start)

#driver code
list1=[]
f1 = open("data1.txt", "r")
for i in f1:
  i = [] #iterating through line by line
  list1.append(i) #appending each line to the list
selection_sort(list1) #calling 2 functions
insertion_sort(list1)
