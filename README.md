# 26thmay_B1_devops_python
## day 1
Task 1
```
import ctypes
a = 10
address = id(a)
print(ctypes.cast(address,ctypes.py_object).value)
```
