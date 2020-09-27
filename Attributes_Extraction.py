import PyPDF2
import re

  
def find_shape(paragraph,start):
    global previous
    pattern = f'.+?(?=\*{start})'
    search= re.search(pattern,paragraph)
    if(search==None):
        return previous
    else:
        previous=search.group()
        return previous
    
    
def find_museum(paragraph,start):
    pattern= f'(\*{start}.+?(?=\. Ht|ht))|({start}.+?(?=\. Ht|ht))'
    search = re.search(pattern,paragraph)
    if(search==None):
        pattern= f'(\*{start}.+?(?=\. [A-Z]))|({start}.+?(?=\. [A-Z0-9]))'
        search= re.search(pattern,paragraph)
        if(search==None):
            return None
        else:
            return search.group().replace(f'*{start}','').strip()
    else:
        return search.group().replace(f'*{start}','').strip()
    
def find_dimension(paragraph):
    pattern = '(Ht|ht).+?(?=[A-Z])'
    search = re.search(pattern,paragraph)
    if (search==None):
        search = re.search('\. \d.+?(?:x).+?(\.)',paragraph)
        if(search==None):
            return None
        else:
            return search.group(),search.span()
    else:
        return search.group(),search.span()
    
def find_plate(paragraph):
    search= re.search('(PLATE.+?(?=[A-Z]))|(PLATED.+?(?=[A-Z]+))',paragraph)
    if(search==None):
        return None
    else:
        return search.group(),search.span()
    
def find_extras_old(paragraph):
    search=re.search('(PLATE.+?(?= \([a-z]\)))|(PLATE.+?(?=\. \([a-z]\)))|(PLATE.+?(?=\. [A-Z][A-Za-z]))',paragraph)
    if(search==None):
        return None
    else:
        return search.group(),search.span()
    
def find_extras(paragraph):
    #search = re.search('((PP|PAdd|PPSupp).+?(?:fig\. [0-9]+))|((PP|PAdd|PPSupp).+?(?=\. \([a-z]\)))|((PP|PAdd|PPSupp).+?(?=\. [A-Z][A-Za-z]+))',paragraph)
    search = re.search('((PP|PAdd|PPSupp).+?(?=\. \([a-z]\)))|((PP|PAdd|PPSupp).+?(?:fig\. [0-9]+))|((PP|PAdd|PPSupp).+?(?=\. [A-Z][A-Za-z]+))',paragraph)
    if(search==None):
        #search=re.search('(PLATE.+?(?= \([a-z]\)))|(PLATE.+?(?=\. \([a-z]\)))|(PLATE.+?(?=\. [A-Z][A-Za-z]))',paragraph)
        search=re.search('(PLATE.+?(?= \([a-z]\)))',paragraph)
        if (search==None):
            search = re.search('PLATE.+?(?=[A-Z])',paragraph)
            if(search==None):
                return None
            else:
               return search.group(),search.span()
        else:
            return search.group(),search.span()
    else:
        return search.group(),search.span()
    
    
    
def text_extractor(path):
    #regex = r"(\*1 )(.+?)(PLATE.+?)(?=( 2 | *2 | The | On | With))"
    out=open("arch.txt",'a')
    with open(path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f,strict=False)
        whole_text = ''
        for i in range(25):
            page = pdf.getPage(i)
            text = page.extractText()
            whole_text = whole_text + text
            '''array =['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','22','23','24','25','26','27',
                    '28','29','30','31','32','33','34','35','36','37','38','39','41','42','43','44','45','46','47',
                    '50','51','52','53','54','55','56','57','58']
            '''
            
        previous=''
        for i in range(1,58):
            start = int(i)
            end = int(i)+1
            pattern = f"(Fragments|Fragment \(.+\)| Lebes gamikos| Squat lekythos| [a-zA-Z]+-[a-zA-z]+| [a-zA-Z]+|) (\*{start} )(.+?)((PLATE|Plate).+?)(?=( \*{end} | {end} | The|6The | On | With))"
            sear= re.search(pattern,whole_text)
            if (sear==None):
                pattern2 = f'{start} .+?(?=(\*{end} | {end} | The | On | With))'
                search2 = re.search(pattern2,whole_text)
                paragraph =search2.group()
                paragraph= paragraph[0:paragraph.rindex('.')].replace('[','(')
                print(paragraph)         
                print("___________________")
                print('vase shape')
                vase_shape=find_shape(paragraph,start)
                museum = find_museum(paragraph,start)
                dimension=find_dimension(paragraph)
                extras = find_extras(paragraph)
                plate = find_plate(paragraph)
                if(extras!=None):
                    span=extras[1]
                    print(vase_shape,'|',museum,'|',dimension,'|',plate,'|',extras,'|',paragraph[span[1]:])
                elif(plate!=None):
                    span=plate[1]
                    print(vase_shape,'|',museum,'|',dimension,'|',plate,'|','NO EXTRAS','|',paragraph[span[1]:])
                elif(dimension!=None):
                    span= dimension[1]
                    print(vase_shape,'|',museum,'dimension:',dimension,'|','NO PLATES','|','NO EXTRAS','|',paragraph[span[1]:])
                      
                print("\n\n")
            else:
                paragraph=sear.group().strip() 
                paragraph= paragraph[0:paragraph.rindex('.')].replace('[','(')
                print(paragraph)
                
                print("_____________________")
                print('vase shape')
                vase_shape=find_shape(paragraph,start)
                museum = find_museum(paragraph,start)
                dimension=find_dimension(paragraph)
                plate = find_plate(paragraph)
                extras = find_extras(paragraph)
                if(extras!=None):
                    span=extras[1]
                    print(vase_shape,'|',museum,'|',dimension,'|',plate,'|',extras,'|',paragraph[span[1]:])
                elif(plate!=None):
                    span=plate[1]
                    print(vase_shape,'|',museum,'|',dimension,'|',plate,'|','NO EXTRAS','|',paragraph[span[1]:])
                elif(dimension!=None):
                    span= dimension[1]
                    print(vase_shape,'|',museum,'|',dimension,'|','NO PLATES','|','NO EXTRAS','|',paragraph[span[1]:])
                print("\n\n")
                s, e = sear.span()
                whole_text = whole_text[e-30:]
               

text_extractor('newRvp3.pdf')