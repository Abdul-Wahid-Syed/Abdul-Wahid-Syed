from itertools import combinations

def sub_set_sum(size, my_array, sub_set_sum):

   for i in range(size+1):
      for my_sub_set in combinations(my_array, i):

         if sum(my_sub_set) == sub_set_sum:
            print(list(my_sub_set))

my_list=[]
# my_list = [21, 32, 56, 78, 45, 99, 0]
my_size =int(input("Number of elements in array:"))
for i in range(0,my_size):
   l=int(input())
   my_list.append(l)
print("The list is :")
print(my_list)
subset_sum = int(input("Enter the desired sweetness level: "))
print("The result is :")
sub_set_sum(my_size, my_list, subset_sum)