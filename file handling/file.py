#here we're opening the file for writing, hence "W"
bo = open('/home/net/MORYSO/PYTHON/class tutorials/Beginner/file handling/b.txt','w')
bo.write('This is the file I want to use in python')
bo.close()

#reading the file
bo = open('/home/net/MORYSO/PYTHON/class tutorials/Beginner/file handling/b.txt','r')
bo.read()
