#!/usr/bin/python3
""" 1-my_list.py """


class MyList(list):
    """ subclass of list """

    def print_sorted(self):
        """ prints the list in sorted order """

        self.mList = self.copy()
        self.mList.sort()
        print(self.mList)
