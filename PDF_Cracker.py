import PyPDF2
#this opens the file

dictionary = open("/Users/davidjpetullo/Desktop/dictionary.txt", 'r')
passwords = dictionary.read().split('\r\n')
#dictionary = ["Joe", "James", "Lilly", "TSDLKGdga", "Sara", "David"]

#pdfReader = PyPDF2.PdfFileReader(open('/Users/davidjpetullo/Documents/MyEncryptedPDF.pdf', 'rb'))
pdfReader = PyPDF2.PdfFileReader(open('/Users/davidjpetullo/Documents/MyEncrypted1.pdf', 'rb'))
for password in passwords:
    #print repr(password)
    result = pdfReader.decrypt(password)
    if result == 0:
        continue
    elif result == 1:
        print "The password is ", password
        break
