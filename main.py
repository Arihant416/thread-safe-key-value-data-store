import time  # This module will be responsible for expiration of a key
import threading
from threading import*

# Global Dictionary/Hashtable to store the data in key-value pair
DATASTORE = {}

# overall file size i.e DATASTORE's size shouldn't exceed 1GB
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
   if key in DATASTORE:
      print("Error: Key exists already")
   else:
      if key.isalpha():
         if (len(DATASTORE) < MAXFILESIZE) and (value <= MAXJSONSIZE):
            if timeout:
               currentFile = [value, time.time()+timeout]
            else:
               currentFile = [value, timeout]
            if len(key) <= 32:
               DATASTORE[key] = currentFile
         else:
            print("Error: Oops!! Memory Limit Exceeded")
      else:
         print("Error: Invalid Key Type, a key needs to consists alphabets only")


'''
Read operation, basic checks:
1) If key in datastore,
2) If key did not expire
Invoke using- read(key_name)
'''
def read(key):
   if key not in DATASTORE:
      print("Error 404: Item not found, please enter valid key")
   else:
      key_value, key_expiration = DATASTORE[key]
      readable = str(key) + ": " +str(key_value)
      if key_expiration != 0:
         if time.time() < key_expiration:
            return readable
         else:
            print("Error Timeout: Key expired")
      else:
         return readable


'''
Update Operation, basic checks
1) If key expired
2) If value replacing meets requirements
3) If key in datastore
Invoke using- update(key, value)
'''
def update(key, value):
   if key in DATASTORE:
      currentValue, currentExpiration = DATASTORE[key]
      if currentExpiration != 0:
         if time.time() < currentExpiration:
            DATASTORE[key] = [value, currentExpiration]
         else:
            print("Error Timeout: Key Expired")
      else:
         DATASTORE[key] = [value, currentExpiration]
   else:
      print("Error 404: Key not found in data-store")


'''
Delete operation, basic checks:
1) If key is present in datastore
2) If key expired
Invoke using- delete(key)
'''
def delete(key):
   if key in DATASTORE:
      value, expiration = DATASTORE[key]
      if expiration != 0:
         if time.time() < expiration:
            del DATASTORE[key]
            print("Success: Key deleted successfully")
         else:
            print("Error Timeout: Key Expired")
      else:
         del DATASTORE[key]
         print("Success: Key deleted successfully")
   else:
      print("Error 404: Key not found in data-store")

