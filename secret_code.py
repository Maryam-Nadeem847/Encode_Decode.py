ask_user = int(input("Please lemme know whether you want to:\n1. Encode a message\n2. Decode a message\nEnter 1 for encoding or 0 for decoding: "))

#Encoding
if(ask_user == 1):
  msg = input("Enter your message to encode: ")
  words = msg.split()   #To separate each word as a string
  random = ["ghq","cwl"]
  i = 0
  new_msg = []
  for word in words:
    if(len(word) >= 3):
      encrypt = random[i] + word[1 : ] + word[0] + random[i + 1]
      new_msg.append(encrypt)
    elif (len(word) < 3):
      new_msg.append(word[::-1])
    else:
      print("You didn't write any message")
  print(" ".join(new_msg))  

#decoding
elif (ask_user == 0):
  msg = input("Enter your message to decode: ")
  words = msg.split()
  new_msg = []
  for word in words:
    if (len(word) >= 3):
      decode = word[3 : -3]   #removed first 3 and last 3 characters
      decode = decode[-1] + decode[:-1]  
      new_msg.append(decode)
    else:
      new_msg.append(word[::-1])
  print(" ".join(new_msg))
