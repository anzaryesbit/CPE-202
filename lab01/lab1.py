# CPE 202 Lab 1

# Maybe_List is either
# Python List
# or
# None

# Maybe_integer is either
# integer
# or
# None

# Maybe_List -> Maybe_integer
def max_list_iter(int_list):
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   elif len(int_list) == 0:
      return None
   else:
      max_value = int_list[0]
      for num in int_list:
         if num > max_value:
            max_value = num
      return max_value

# Maybe_List -> Maybe_List
def reverse_list(int_list):
   """reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   if len(int_list) == 0:
      return []
   if len(int_list) == 1:
      return int_list
   return [int_list[-1]] + reverse_list(int_list[:-1])

# Maybe_List -> None
def reverse_list_mutate(int_list):
   """reverses a list of numbers, modifying the input list, returns None
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError
   if len(int_list) == 0:
      return []
   n = -1
   for i in range(len(int_list)//2):
      temp = int_list[i]
      int_list[i] = int_list[n]
      int_list[n] = temp
      n -= 1
   return int_list

