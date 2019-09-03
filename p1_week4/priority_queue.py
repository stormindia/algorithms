class Node:

	def __init__(self, data):

		self.data = data
		self.next = None


class queue_using_linkedlist:
	def __init__(self):
		self.tail = None


	def print_queue(self):

		
		if(self.tail is None):
			print("empty list!")
			return
		else:
			curr_element = self.tail
			while(curr_element != None):
				print(curr_element.data)
				curr_element = curr_element.next

		return


	#making queue s.t. tail always points at the latest element
	def enqueue(self, data):

		new_node = Node(data)

		new_node.next = self.tail

		self.tail = new_node


	#using above enqueue method, we can use same dequeue method as pop 	
	def dequeue(self):
		if(self.tail is None):
			print("list is empty")
			return False

		curr_element = self.tail
		prev_element = None
		value = None
		while(curr_element.next != None):
			
			prev_element = curr_element
			curr_element = curr_element.next
			value = curr_element.data
		
		prev_element.next = None


		print("front most(or max if delMax) element with value {} popped".format(value))
		return True

	def find(self, data):

		position = 1

		if(self.tail is None):
			print("list is empty")
			return False

		curr_element = self.tail

		while(curr_element.data != data):

			if(curr_element.next is None):
				print("element not present")
				return False
			curr_element = curr_element.next
			position = position + 1

		print("element present at position {}".format(position))
		return True


	def delMax(self):		

		if(self.tail is None):
			print("empty list!")
			return
		else:
			
			curr_element = self.tail
			max_element = curr_element
			value = None
			while(curr_element.next != None):
				
				if(max_element.data < curr_element.data):
					max_element = curr_element

				curr_element = curr_element.next
			
			
			#exchange curr_element with max_element
			tmp = curr_element.data
			curr_element.data = max_element.data
			max_element.data = tmp

			self.dequeue()


		return



queue_1 = queue_using_linkedlist()

queue_1.enqueue(5)
queue_1.enqueue(7)
queue_1.enqueue(6)



queue_1.print_queue()

queue_1.delMax()


queue_1.print_queue()
