# Methods in the array module

from array import array

# append()
a = array('i', [10, 20, 30])
a.append(40)
print("append:", a)

# buffer_info()
a = array('i', [10, 20, 30])
print("buffer_info:", a.buffer_info())

# byteswap()
a = array('i', [10, 20, 30])
a.byteswap()
print("byteswap:", a)

# count()
a = array('i', [10, 20, 10, 30, 10])
print("count:", a.count(10))

# extend()
a = array('i', [10, 20, 30])
a.extend([40, 50])
print("extend:", a)

# frombytes()
a = array('i', [10, 20, 30])
data = a.tobytes()
b = array('i')
b.frombytes(data)
print("frombytes:", b)

# fromfile()
a = array('i', [10, 20, 30])
file = open("numbers.txt", "wb")
a.tofile(file)
file.close()

b = array('i')
file = open("numbers.txt", "rb")
b.fromfile(file, 3)
file.close()
print("fromfile:", b)

# fromlist()
a = array('i')
a.fromlist([10, 20, 30, 40])
print("fromlist:", a)

# fromunicode()
a = array('u')
a.fromunicode("hello")
print("fromunicode:", a)

# index()
a = array('i', [10, 20, 30, 40])
print("index:", a.index(30))

# insert()
a = array('i', [10, 20, 40])
a.insert(2, 30)
print("insert:", a)

# pop()
a = array('i', [10, 20, 30, 40])
a.pop()
print("pop:", a)

# remove()
a = array('i', [10, 20, 30, 40])
a.remove(20)
print("remove:", a)

# reverse()
a = array('i', [10, 20, 30, 40])
a.reverse()
print("reverse:", a)

# tobytes()
a = array('i', [10, 20, 30])
data = a.tobytes()
print("tobytes:", data)

# tofile()
a = array('i', [10, 20, 30])
file = open("numbers2.txt", "wb")
a.tofile(file)
file.close()
print("Array saved to file")

# tolist()
a = array('i', [10, 20, 30])
b = a.tolist()
print("tolist:", b)

# tounicode()
a = array('u')
a.fromunicode("hello")
print("tounicode:", a.tounicode())
