"""
Write code to remove duplicates from a sorted linked list.
"""

# Node class 
class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList(): 

	def __init__(self): 
		self.head = None

	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def deleteNode(self, key): 
		 
		cur = self.head 

		# If head node itself holds the 
		# key to be deleted 
		if (cur is not None): 
			if (cur.data == key): 
				self.head = cur.next
				cur = None
				return

		# Search for the key to be deleted, 
		# keep track of the previous node as 
		# we need to change 'prev.next' 
		while(cur is not None): 
			if cur.data == key: 
				break
			prev = cur
			cur = cur.next

		# if key was not present in 
		# linked list 
		if(cur == None): 
			return

		# Unlink the node from linked list 
		prev.next = cur.next

		cur = None

	# Utility function to print the 
	# linked LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print(temp.data , end = ' ') 
			temp = temp.next
	
	# This function removes duplicates 
	# from a sorted list		 
	def removeDuplicates(self): 
		temp = self.head 
		if temp is None: 
			return
		while temp.next is not None: 
			if temp.data == temp.next.data: 
				new = temp.next.next
				temp.next = None
				temp.next = new 
			else: 
				temp = temp.next
		return self.head 

# Driver Code 
llist = LinkedList() 

llist.push(20) 
llist.push(13) 
llist.push(13) 
llist.push(11) 
llist.push(11) 
llist.push(11) 
print ("Created Linked List: ") 
llist.printList() 
print() 
print("Linked List after removing", 
			"duplicate elements:") 
llist.removeDuplicates() 
llist.printList() 

# This code is contributed by 
# Dushyant Pathak. 
