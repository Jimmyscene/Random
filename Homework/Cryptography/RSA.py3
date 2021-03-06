def Encrypt(Plaintext,pubkey=71,p=151,q=271):
	triagraph=[]
	for i in range(1,1+(len(Plaintext)//3)):
		triagraph.append(Plaintext[3*(i-1):3*i])
	if(len(Plaintext)%3!=0):
		triagraph.append(Plaintext[-(len(Plaintext)%3):])
	codes=[toInt(x) for x in triagraph]
	return ("".join(([toQuadragraph(encodeTriagraph(code,pubkey,p,q)) for code in codes])))

def toInt(Triagraph):
	Triagraph=list(Triagraph)
	Triagraph.reverse()
	temp=0
	i=0
	for num in Triagraph:
		temp+=((ord(num)-65)*26**i)
		i+=1
	return temp

def encodeTriagraph(code,pubkey,p,q):
	code=(code**pubkey)%(p*q)
	return code

def toQuadragraph(code):
	return(str(chr((code//(26**3))+65)+ chr(((code%26**3)//26**2)+65)+ chr((((code%26**3)%26**2)//26)+65)+ chr((((code%26**3)%26**2)%26)+65)))


def Decrypt(CipherText,privatekey=14831,p=151,q=271):
	quadragraph=[]
	for x in range(1,(len(CipherText)//4)+1):
		quadragraph.append(CipherText[4*(x-1):4*x])
	if(len(CipherText)%4!=0):
		quadragraph.append(CipherText[-(len(CipherText)%4):])
	codes=[]
	for x in range(len(quadragraph)):
		codes.append(encodeQuadraph(toInt(quadragraph[x]),privatekey,p,q))
	Plaintext=''
	for code in codes:
		Plaintext+=decipherquadraph(code)

	return(Plaintext)

def encodeQuadraph(code,privatekey,p,q):
	return ((code**privatekey)%(p*q))

def decipherquadraph(code):
	first=chr((code//26**2)+65)
	second=chr(((code%26**2)//26)+65)
	third=chr((code%26**2)%26+65)
	return(str(first+second+third))


if __name__ == '1__main__':
	choice=input("Would you like to input your own unique primes, public and private key?\n These numbers will not be checked and may cause errors. (Y/N)\n:")
	while(True):
		if(choice=='Y'):
			message=input("Please input a string to encrypt. No spaces or punctuation please.\n\n:").upper()

			p=int(input("Select a prime number. \n:"))
			q=int(input("Select one more prime number. \n:"))
			public=int(input("Select a public key. \n:"))
			private=int(input("Select a private key. \n:"))
			
			print("\n\nEncrypted: ", Encrypt(message,public,p,q))
			print("Decrypted: ", Decrypt(Encrypt(message,public,p,q),private,p,q))
			exit()
		if(choice=='N'):
			print("Standard values will be used instead.")
			message=input("Please input a string to encrypt. No spaces or punctuation please.\n:").upper()
			print("\n\nEncrypted: ", Encrypt(message))
			print("Decrypted: ", Decrypt(Encrypt(message)))
			exit()
		else:
			choice=input("Please Use Only 'Y' Or 'N'\n:")
if __name__ == '__main__':
	print(Decrypt(Encrypt("thingsarecooltoday".upper())))