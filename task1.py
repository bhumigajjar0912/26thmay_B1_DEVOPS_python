import ctypes
a = 10
address = id(a)
print(ctypes.cast(address,ctypes.py_object).value)