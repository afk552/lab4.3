#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Python program invoking a
# method using super()
from abc import ABC


class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        print("subclass")


if __name__ == '__main__':
    r = K()
    r.rk()
