#!/usr/bin/python3
<<<<<<< HEAD
"""Singly linked list class, in python"""


class Node:
    """Node of a singly linked list"""
    def __init__(self, data=0, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data"""
        if type(value) is not int:
=======
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialise a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/sets the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
<<<<<<< HEAD
        """return next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
=======
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
<<<<<<< HEAD
    """SLL head and functions"""

    def __init__(self):
        self.__head = None

    def __repr__(self):
        retstr = ""
        if self.__head is None:
            pass
        else:
            ptr = self.__head
            while ptr is not None:
                retstr += str(ptr.data) + '\n'
                ptr = ptr.next_node
        return retstr[:-1]

    def sorted_insert(self, value):
        """inserts a linked list node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            ptr = self.__head
            while ptr.next_node is not None and ptr.next_node.data < value:
                ptr = ptr.next_node
            if ptr.next_node is None:
                ptr.next_node = Node(value)
            else:
                ptr.next_node = Node(value, ptr.next_node)
=======
    """Represents a singly-linked list."""

    def __init__(self):
        """Initalizes a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Defines the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
>>>>>>> df6dd911fde4d8be9b455210d2432b7486f4901a
