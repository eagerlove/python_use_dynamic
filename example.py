import ctypes

lib = ctypes.cdll.LoadLibrary('./libexam.so')

result = lib.add(1, 2)
result2 = lib.minus(1, 3)
print(result)
