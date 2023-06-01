#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Python program showing
# implementation of abstract
# class through subclassing
import abc


class parent:
    def geeks(self):
        pass


class child(parent):
    def geeks(self):
        print("child class")


if __name__ == '__main__':
    print(issubclass(child, parent))
    print(isinstance(child(), parent))
