#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


"""
class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p
"""


class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        super().__init__(l, w, h)
        self.places = p


if __name__ == '__main__':
    t4 = KitchenTable(1.5, 2, 0.75, 6)
    print(t4.height)
