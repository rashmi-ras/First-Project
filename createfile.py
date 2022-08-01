try:
    f=open("myfile.txt","x")
    print("file created successfully")
except:
    print("file exist")