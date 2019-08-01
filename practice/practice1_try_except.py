try:
    file=open("testfile.txt","w")
    file.write("this is a test file for try except practice")
except IOError:
    print("沒這個文件阿")
else:
    print('found it and write correctly!')
    file.close()
