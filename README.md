# Data Structures

# Linked List
##Module: linked_list.py
##Test Module: test_linked_list.py

This module consists of a Node class, which can be instantiated to create node instances. It also includes a LinkedList class, which can take a node as input, and create a linked list with that node as the head of the list. 

The module's *push()* method adds nodes to the list, connecting them to the list's head node, and creating a true linked list.

The module's *pop()* method removes the head of the list and returns it, and makes the next node the new head of the linked list.

The *size()* returns the length of the linked list, in number of nodes.

The *search()* method iterates through the linked list for a particular value and returns that value. If the value wasn't in the list, the method returns an error message.

The *remove()* method takes in a node, iterates through the list to find the node, removes it if it is present, and reattaches the pointer from the node before the deleted node to the node following the deleted node. 

The *display()* method accepts a linked list, and returns a string representing a tuple of the list values.



## We relied on the following resources in building our linked list and associated functions.

1. http://stackoverflow.com/questions/280243/python-linked-list
2. http://greenteapress.com/thinkpython/html/chap17.html
3. http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
4. https://codefellows.github.io/sea-python-401d5/assignments/linked_list.html

We also received help from Claire and Amos! 