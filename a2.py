amount= int(input("Enter your amount : "))

notes200= amount // 200
amount= amount % 200

notes100= amount // 100
amount= amount % 100

print ("200 notes : " ,notes200 )
print ("100 notes : ", notes100)