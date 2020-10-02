import PyPDF2
import re
from Paragraph import Paragraph
class pdf_extractor:
    def __init__(self,file_path):
        self.file_path=file_path
        self.whole_text=''
        self.paragraphs_list=[]
    

    def load_text(self):
        with open(self.file_path,'rb') as f:
            pdf = PyPDF2.PdfFileReader(f,strict=False)
            for i in range(25):
                page = pdf.getPage(i)
                text = page.extractText()
                self.whole_text= self.whole_text + text
            #corrections in the whole text
            self.whole_text=self.whole_text.replace('Š','-').replace('THE RED-FIGURED VASES OF PAESTUM','').replace('I9','19')
            
            

    def get_paragraphs(self):
            self.load_text()
            for i in range(1,58):
                start = int(i)
                end = int(i)+1
                pattern = f"(Fragments|Fragment \(.+\)| Lebes gamikos| Squat lekythos| [a-zA-Z]+-[a-zA-z]+| [a-zA-Z]+|) (\*{start} )(.+?)((PLATE|Plate).+?)(?=( \*{end} | {end} | The|6The | On | With))"
                search= re.search(pattern,self.whole_text)
                if(search==None):
                    pass
                    pattern2 = f'{start} .+?(?=(\*{end} | {end} | The | On | With))'
                    search2= re.search(pattern2,self.whole_text)
                    paragraph =search2.group()
                    paragraph= paragraph[0:paragraph.rindex('.')].replace('[','(')
                    para_object = Paragraph(paragraph,start)
                    self.paragraphs_list.append(para_object)
                else:
                    paragraph=search.group().strip() 
                    paragraph= paragraph[0:paragraph.rindex('.')].replace('[','(')
                    para_object = Paragraph(paragraph,start)
                    self.paragraphs_list.append(para_object)
                    s, e = search.span()
                    self.whole_text = self.whole_text[e-30:]
            return self.paragraphs_list

if(__name__=='__main__'):  
    pdf_ex = pdf_extractor('./newRVp3.pdf')
    p_list=pdf_ex.get_paragraphs()
    out = open('demo1.txt','a')
    for i in p_list:
        print(i)
        x=i.get_attributes()
        out.write(str(x))
        out.write('\n_____________\n')
        print('*************')
    out.close()
                    



    