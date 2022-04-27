# handle = open("test.txt", "r" )
# data = handle.readline() #! can be readline/read/redlines
# print(data)
# handle.close()

# handle = open("test.txt","r")
# data = handle.read()
# counter = 0
# for word in data.split():
#     if word == "Python":
#        counter += 1
# print(counter)

# handle = open("test-write.txt", "w")

# handle.write("Hello Moringa")
# handle.close()

#!with block
with open("test.txt", "r") as handle:
  data = handle.read()
print(data)