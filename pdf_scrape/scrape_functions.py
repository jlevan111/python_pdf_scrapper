
print("First Line")
import PyPDF2 
import gui
 
gui.service_func()

print("First Line")
# creating a pdf file object 
pdfFileObj = open(r'C:\Users\josh_\Downloads\transaction_34978351.pdf', 'rb') 
 
# creating a pdf reader object 
pdfReader = PyPDF2.PdfReader(pdfFileObj)
# creating a page object 
pageObj = pdfReader.pages[0] 
 
gui.service_func()

res=pageObj.extract_text()
res_split = res.split()
# extracting text from page 
print(str(res_split))
length_input = len(res_split)
print(length_input)
i=0
while i<length_input:
 print(res_split[i])
 i+=1
 

    

# closing the pdf file object 
pdfFileObj.close()