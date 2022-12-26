#!/usr/bin/python3
""" A singly linked list module """


class Node:
    """ The node class of the list """

    def __init__(self, data, next_node=None):
        if type(data) is int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")
        if type(next_node) is Node or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """ return the data """
        return self.__data

    @data.setter
    def data(self, val):
        """ set the value of data to val """

        if type(data) is int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ return the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, nxt):
        if type(nxt) is Node or nxt is None:
            self.__next_node = nxt
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ A class for singly linked list """

    def __init__(self):
        """ simple init """
        self.__head = None

    def sorted_insert(self, val):
        """ insert node in a sorted fashion """
        if self.__head is None and type(val) is int:
            self.__head = Node(val)
        elif type(val) is int:
            temp = self.__head
            prev = None
            while temp is not None and val > temp.data:
                prev = temp
                temp = temp.next_node
            if prev is not None:
                new = Node(val)
                new.next_node = temp
                prev.next_node = new
            else:
                new = Node(val)
                new.next_node = temp
                self.__head = new

    def __str__(self):
        """ the string representation of the list """
        temp = self.__head
        while temp is not None and temp.next_node is not None:
            print(temp.data)
            temp = temp.next_node
        if temp is not None:
            return str(temp.data)
        else:
            return ""
