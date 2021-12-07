"""
this code encrypts into caesar cipher given the substitution shifts and if the letter is a small or capital letter. why? why 
won't i use an online tool like a normal lazy programmer? I'm bored :-(
"""
#we begineth by defining the shifts....we could ask the user for it but, im too lazy to do that so....
shift = 3
#then we input the text to be encrypted or ask the user if you have the strength to do that
text = "Hello World"
#this is where after encryption the encrypted letter will be appended
encryption = ""

#put the loop here 
#l represents the letters on the text
for l in text:
    #check if the character is a capital or small letter
    if l.isupper():
        #find the position in the unicode thingy
        l_unicode = ord(l)
        l_index = ord(l)-ord("A")

        #perform the shift using the ccer(c=(x+n)%26)
        new_index = (l_index+shift) % 26
        #convert to new character
        new_unicode = new_index + ord("A")
        #convert the new unicode into its character representation
        new_character = chr(new_unicode)

        #append to encrypted string
        encryption = encryption + new_character
    elif l==" ":
        pass

    else:
        #the characteris not in upper case
        l_unicode = ord (l)
        l_index =ord (l)-ord("a")
        new_index = (l_index + shift)% 26
        new_unicode = new_index + ord("a")
        new_character = chr(new_unicode)
        encryption = encryption + new_character



print ("Plain text: ", text)
print ("Encrypted text: ", encryption)
# i need to find a way to ensure that the spac bar is encluded before i go on to the decryption part but i'm to lazy to do it rn so bye....
# decryption is basically doing the inverse of the above process but using the rule (x = (c-n)% 26)
#
