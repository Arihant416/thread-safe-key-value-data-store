import time  # This module will be responsible for expiration of a key
import threading
from threading import*

# Global Dictionary/HASHTABLE to store the data in key-value pair
HASHTABLE = {}

# overall file size i.e hashtable's size shouldn't exceed 1GB
MAXFILESIZE = 1024 * 1024 * 1024

# MAXSIZE for JSON Object
MAXJSONSIZE = 16 * 1024 * 1024


# Creating a key-value pair, timeout is optional
'''
Checks to perform 
1) Size of file less than 1GB i.e 1024*1024*1024
2) Size of JSON Object is less than 16KB i.e 
3) If key exists & is alphabet process creation
'''


def create(key, value, timeout = 0):
   if key in HASHTABLE:
      print("Error: Key exists already")
   else:
      if key.isalpha():
         if (len(HASHTABLE) < MAXFILESIZE) and (value <= MAXJSONSIZE):
            if timeout:
               currentFile = [value, time.time()+timeout]
            else:
               currentFile = [value, timeout]
         else:
            print("Error: Oops!! Memory Limit Exceeded")
      else:
         print("Error: Invalid Key Type, a key needs to consists alphabets only")
