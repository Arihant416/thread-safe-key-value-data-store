import time  # This module will be responsible for expiration of a key
import threading
from threading import*

# Global Dictionary/HASHTABLE to store the data in key-value pair
HASHTABLE = {}

# overall file size i.e hashtable's size shouldn't exceed 1GB
MAXFILESIZE = 1024 * 1024 * 1024

# MAXSIZE for JSON Object
MAXJSONSIZE = 16 * 1024 * 1024



'''
Create operation, basic checks
1) Size of file less than 1GB i.e 1024*1024*1024
2) Size of JSON Object is less than 16KB i.e 
3) If key exists & is alphabet process creation

Invoke using - create(key, value, optional_timeout)
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
            if len(key) <= 32:
               HASHTABLE[key] = currentFile
         else:
            print("Error: Oops!! Memory Limit Exceeded")
      else:
         print("Error: Invalid Key Type, a key needs to consists alphabets only")


'''
Read operation, basic checks:
1) If key in Hashtable,
2) If key did not expire

Invoke using- read(key_name)
'''
def read(key):
   if key not in HASHTABLE:
      print("Error 404: Item not found, please enter valid key")
   else:
      key_value, key_expiration = HASHTABLE[key]
      readable = str(key) + ": " +str(key_value)
      if key_expiration != 0:
         if time.time() < key_expiration[1]:
            return readable
         else:
            print("Timeout: Key expired")
      else:
         return readable


'''
Update Operation, basic checks
1) If key expired
2) If value replacing meets requirements
3) If key in Hashtable
Invoke using- update(key, value)
'''
def update(key, value):
   if key in HASHTABLE:
      currentValue, currentExpiration = HASHTABLE[key]
      if currentExpiration != 0:
         if time.time() < currentExpiration:
            HASHTABLE[key] = [value, currentExpiration]
         else:
            print("Error Timeout: Key Expired")
      else:
         HASHTABLE[key] = [value, currentExpiration]
   else:
      print("Error 404: Key not found in data-store")
   
