import ctypes

lib = ctypes.cdll.LoadLibrary('./libexam.so')

result = lib.add(1, 2)

print(result)
