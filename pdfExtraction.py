import PyPDF2
import re

   
def text_extractor(path):
    out=open("arch.txt",'a')
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f,strict=False)
        whole_text = ''
        for i in range(25):
            page = pdf.getPage(i)
            text = page.extractText()
            whole_text = whole_text + text
            array =['1','2','3','4','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','22','23','24','25','26','27',
                    '28','29','30','31','32','33','34','35','36','37','38','39','41','42','43','44','45','46','47',
                    '50','51','52','53','54','55','56','57','58']
        for i in array:
            start = int(i)
            end = int(i)+1
            #pattern = f'(\*{start} )(.+?)((PLATE|Plate).+?)(?=( \*{end} | {end} | The|6The | On | With))'
            pattern = f"(Fragments|Fragment \(.+\)| Lebes gamikos| Squat lekythos| [a-zA-Z]+-[a-zA-z]+| [a-zA-Z]+|) (\*{start} )(.+?)((PLATE|Plate).+?)(?=( \*{end} | {end} | The|6The | On | With))"
            sear= re.search(pattern,whole_text)
            if (sear==None):
                pattern2 = f' {start} .+?(?=(\*{end} | {end} | The | On | With))'
                search2 = re.search(pattern2,whole_text)
                paragraph =search2.group()
                print(paragraph)
                print("___________________")
            else:
                paragraph=sear.group()
                print(paragraph)
                print("_____________________")
                s, e = sear.span()
                whole_text = whole_text[e-30:]
               

text_extractor('newRvp3.pdf')