class Node:

	def __init__(self, data):

		self.data = data
		self.next = None

class linkedlist:
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

	#insert at beginning
	def prepend(self, data):

		new_node = Node(data)

		new_node.next = self.head

		self.head = new_node


	#insert at last	
	def append(self, data):
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
		
		

	def remove(self, data):

		#can't use find function directly as we need to keep a track of previous element as well
		#this is where doubly linked list are better

		if(self.head is None):
			print("list is empty")
			return False

		curr_element = self.head
		prev_element = None
		while(curr_element.data != data):

			if(curr_element.next is None):
				print("element not present")
				return False

			prev_element = curr_element
			curr_element = curr_element.next


		#first element itself	
		if(curr_element is self.head):
			self.head = curr_element.next
			curr_element.next = None

		#last element
		elif(curr_element.next is None):
			prev_element.next = None

		#in between element
		else:
			prev_element.next = curr_element.next
			curr_element.next = None

		print("element removed")
		return True


	def insert_at_random(self,data,position):

		new_node = Node(data)

		if(position == 0): #insert at beginning
			self.prepend(data)
			return

		curr_element = self.head
		curr_position = 0
		new_node_next_element = self.head.next

		while(curr_position != position-1):
			curr_element = curr_element.next
			curr_position = curr_position + 1

			if(curr_element.next is None and curr_position != position):
				print("position value is greater than the length of the stack")
				return False

			if(curr_element.next is None and curr_position == position):
				self.append(data)	#insert at last
				return
		
			new_node_next_element = curr_element.next

		curr_element.next = new_node
		new_node.next = new_node_next_element	



ll1 = linkedlist()

ll1.append(5)
ll1.append(3)
ll1.append(1)
ll1.append(2)
ll1.append(7)
ll1.append(9)

#counting starts from 0 here for this function
ll1.insert_at_random(12,2)
ll1.print_list()
#ll1.find(3)
#ll1.remove(5)
#ll1.print_list()