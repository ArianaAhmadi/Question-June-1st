numbers=input("Please enter a list of numbers:\n").split()

def list_sum(list, size):
   if size == 1:
     return list[0]
   else:
     return list[size - 1,] + list_sum(list, size - 1)
  
  
total = list_sum(numbers, len(numbers))
 
print("Sum of all elements in given list: ", total)

# Can you copy and paste the code you orignaly put here back in, since it worked.


'''
  total=0
  return total+list_sum(v-1)
numbers=input("Please enter a list of numbers:\n").split()

total = 0
numbers=input("Please enter a list of numbers:\n").split()
 
for ele in range(0, len(numbers)):
    total+=int(numbers[ele])
 
print("Sum of all elements in given list: ", total)
'''