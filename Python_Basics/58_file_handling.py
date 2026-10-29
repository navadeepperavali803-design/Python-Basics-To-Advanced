with open("message.txt","w")as file:
    file.write("hello world")
with open("message.txt","r")as file:
    content=file.read()
print(content)