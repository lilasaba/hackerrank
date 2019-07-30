# vim: tabstop=8 expandtab shiftwidth softtabstop=4

import glob
import os
import re
import sys


class Tree(object):
     def __init__(self, name, value=None, children=None, parent=None):
         self.name = name
         self.value = value
         self.children = children or []
         self.parent = parent

     def add_child(self, name):
         new_child = Tree(name, parent=self)
         self.children.append(new_child)
         return new_child

     def is_root(self):
         return self.parent is None

     def is_leaf(self):
         return not self.children

     def get_value(self):
         return self.value

     def set_value(self, newval):
         self.value = newval

     def __iter__(self):
         if self.name != None:
             return iter(self.name)
         else:
             return iter([])

     def __repr__(self):
         return self.name

     def __str__(self):
         if self.is_leaf():
             return str(self.name)
         return '{name} [{children}]'.format(name=self.name, children=', '.join(map(str, self.children)))


def add_edge(tree, parent, child):
     if tree.name == parent:
         out_tree = tree.add_child(child)
     else:
         return add_edge(tree.parent, parent, child)

     return out_tree


def update_tree(tup, tree):
    T, V, K = [int(n) for n in tup[1:]]
    T = str(T)
    pass


def query_tree(tup, tree):
    pass


if __name__ == '__main__':
    inp = '7 7 1\n1 2\n2 3\n2 4\n2 5\n5 6\n6 7\nU 5 10 2\nU 4 5 3\nQ 1 7\nU 6 7 4\nQ 2 7\nQ 1 4\nQ 2 4'

    lines = inp.split('\n')
    tups = [l.split() for l in lines]
    N, E, R = tups[0]
    N = int(N)
    E = int(E)
    edges = [l for l in tups[1:(N-1)]]
    # Init tree.
    t0 = Tree(R)
    t = t0
    for pch in edges:
        p, ch = pch
        t = add_edge(t, p, ch)

    print(t0)
    print(list(t0))
    for tup in tups[-E:]:
        print(tup)
        if tup[0] == 'U':
            update_tree(tup, t0)
        elif tup[0] == 'Q':
            query_tree(tup, t0)


