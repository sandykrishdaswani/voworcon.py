ch=input("Enter Your Character:")
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'  
     or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
  print("The Given Character", ch, "vowel")
elif ch == '$' :
  print("The Given Character", ch, "invalid")
else:
  print("The Given Character", ch, "consonant")
