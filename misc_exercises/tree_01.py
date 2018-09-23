#!/usr/bin/env python
class Tree(object):
    def __init__(self, cargo, left=None, right=None):
        self.left = None
        self.right = None
        self.cargo = None
        
    def __str__(self):
        return str(self.cargo)

