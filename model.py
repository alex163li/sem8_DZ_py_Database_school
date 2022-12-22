def write(data):
    with open('file.csv','a') as file:
        file.writelines(data)
          
def read():
    with open('file.csv','r') as file:
        return file.readlines()
