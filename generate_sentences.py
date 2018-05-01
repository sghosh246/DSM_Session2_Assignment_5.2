# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:10:29 2018
@author: sourav ghosh
"""
"""
Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
"""
subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print("{}{}{}".format(subject+' ',verb+' ',obj))

