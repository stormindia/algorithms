#----------------USING LINKED LISTS START------------------------------------#
class Node:

	def __init__(self, data):

		self.data = data
		self.next = None

class stack_using_linkedlist:
	"""docstring for linkedlist"""
	def __init__(self):
		self.head = None


	def print_list(self):

		#print(self.head.data)

		if(self.head is None):
			print("empty list!")
			return
		else:
			curr_element = self.head
			while(curr_element != None):
				print(curr_element.data)
				curr_element = curr_element.next

	#insert at last	
	def push(self, data):
		new_node = Node(data)

		if(self.head is None):
			self.head = new_node
			return

		curr_element = self.head

		while(curr_element.next is not None):
			curr_element = curr_element.next

		curr_element.next = new_node


	def find(self, data):

		position = 1

		if(self.head is None):
			print("list is empty")
			return False

		curr_element = self.head

		while(curr_element.data != data):

			if(curr_element.next is None):
				print("element not present")
				return False
			curr_element = curr_element.next
			position = position + 1

		print("element present at position {}".format(position))
		return True
		
		

	def pop(self):

		#can't use find function directly as we need to keep a track of previous element as well
		#this is where doubly linked list are better

		if(self.head is None):
			print("list is empty")
			return False

		curr_element = self.head
		prev_element = None
		value = None
		while(curr_element.next != None):
			
			prev_element = curr_element
			curr_element = curr_element.next
			value = curr_element.data
		
		prev_element.next = None


		print("last element with value {} popped".format(value))
		return True

stack_1 = stack_using_linkedlist()

# stack_1.push(5)
# stack_1.push(6)
# stack_1.push(7)

# stack_1.pop()
# stack_1.print_list()

#--------------------USING LINKED LIST END----------------------------------------------------------------#


#--------------------USING RESIZABLE ARRAY----------------------------------------------------------------#

def push_in_array(value,stack=None):

	stack.append(value)

	return

def pop_from_array(stack=None):

	print("popped element is {}".format(stack[-1]))

	#to decrease the size of array --> free memory
	del stack[-1]


stack_1 = [1,2,3,4]

push_in_array(5,stack_1)
print(len(stack_1))

pop_from_array(stack_1)
print(len(stack_1))


#--------------------USING RESIZABLE ARRAY END-------------------------------------------------------------#