# About 
This project can only run on Linux or other systems that support .so dynamic library.

# How I build it
## By using this command
```bash
gcc -fPIC -shared -o libexam.so example.c
```
## then use the .so library in python script
```python
import ctypes
lib = ctypes.cdll.LoadLibrary('./libexam.so')
```
## Completed!

# How to use it
Enter this in your shell:
```bash 
python3 test.py 
```

# Have a good time!
