import re
class Paragraph:
    previous=''
    shape_pattern =f'.+?(?=\*\d)'
    museum_pattern1=f'(\*\d.+?(?=\. Ht|ht))|(\d.+?(?=\. Ht|ht))'
    museum_pattern2=f'(\*\d.+?(?=\. [A-Z]))|(\d.+?(?=\. [A-Z0-9]))'
    dimension_pattern1='(Ht|ht).+?(?=[A-Z])' 
    dimension_pattern2='\. \d.+?(?:x).+?(\.)'
    plate_pattern1='(PLATE.+?(?=[A-Z]))|(PLATED.+?(?=[A-Z]+))'
    extras_pattern1='((PP|PAdd|PPSupp).+?(?=\. \([a-z]\)))|((PP|PAdd|PPSupp).+?(?:fig\. [0-9]+))|((PP|PAdd|PPSupp).+?(?=\. [A-Z][A-Za-z]+))'
    extras_pattern2='(PLATE.+?(?= \([a-z]\)))'
    extras_pattern3='PLATE.+?(?=[A-Z])'

    def __init__(self,text,start):
        self.text = text
        self.attributes = {
            'id':start,
            'shape':'' ,
            'location':'',
            'plate':'',
            'dimension':'',
            'extras':'',
            'description':''

        }
       
    
    def find_match(self,pattern):
        search = re.search(pattern,self.text)
        if (search):
            return search.group(),search.span()

        return search


    def get_shape(self):
        shape = self.find_match(Paragraph.shape_pattern)
        if(shape):
            Paragraph.previous=shape
            return shape
        else:
            return Paragraph.previous

    def get_location(self):
        location = self.find_match(Paragraph.museum_pattern1)
        if(location):
            return location
        else:
            location= self.find_match(Paragraph.museum_pattern2)
            if(location):
                return location
        return None

    def get_dimension(self):
        dimension = self.find_match(Paragraph.dimension_pattern1)
        if(dimension):
            return dimension
        else:
            dimension = self.find_match(Paragraph.dimension_pattern2)
            if(dimension):
                return dimension
        return None
   
    def get_plate(self):
        plate = self.find_match(Paragraph.plate_pattern1)
        if(plate):
            return plate
        return None

    def get_extras(self):
        extras = self.find_match(Paragraph.extras_pattern1)
        if(extras):
            return extras
        else:
            extras = self.find_match(Paragraph.extras_pattern2)
            if(extras):
                return extras
            else:
                extras = self.find_match(Paragraph.extras_pattern3)
                if(extras):
                    return extras
        return None

    def get_description(self):
        extras = self.get_extras()
        plate=self.get_plate()
        dimension=self.get_dimension()

        if(extras):
            span= extras[1]
            return self.text[span[1]:]
        elif(plate):
            span=plate[1]
            return self.text[span[1]:]
        elif(dimension):
            span=dimension[1]
            return self.text[span[1]:]

    def __str__(self):
        return str(self.get_shape()[0])

  

    def format_attributes(self):
        location= self.get_location()
        extras = self.get_extras()
        plate =self.get_plate()
        description = self.get_description()
        shape = self.get_shape()
        dimension = self.get_dimension()
        if (location):
            start=self.attributes['id']
            location= location[0].replace(f'*{start}','').strip()
            self.attributes['location']=location
        if(extras):
            # remove "PLATE" from extras
           if('PLATE' in extras[0]):
                extras = re.sub(r'PLATE.+?(?=[A-Z])', "", extras[0])
                if('PLATE' in extras):
                    self.attributes['extras']=None
                else:
                    self.attributes['extras']=extras
           else:
               self.attributes['extras']=extras[0]
        if(plate):
            #remove (a) from the plates
             plate= re.sub(r'\([a-z]\)',"",plate[0])
             self.attributes['plate']=plate.strip()
        if(shape):
            self.attributes['shape']=shape[0]
        if(dimension):
            self.attributes['dimension']=dimension[0]
        if(description):
            self.attributes['description']=description
        
        return self.attributes
              
        
             


    

    def get_attributes(self):
        formatted_attr = self.format_attributes()
        return formatted_attr

    def get_alan_format(self):
        f = self.format_attributes()
        alan_format = {
             'vase_name': f['shape'],
              'vase_number':f['id'],
               'description':f['description'],
               'dimension':f['dimension'],
               'vase_location':f['location'],
               'vase_plate':f['plate'],
                'vase_extras':f['extras']
        }

        return alan_format


        

if(__name__=='__main__'):

    p = Paragraph('Neck-amphora *1 Geneva HR 29. Ht. 42-3. PLATE 15 Chamay, La Guerre de Troie, pp. 24Š5, ill. on p. 25; Genava 33, 1985, p. 185, fig. 1; Le Peinlre de Darius et son milieu ( 1986), pp. 264Š9, with colour ill. on p. 29; detail, Musees de Geneve 265, May 1986, p. 17. (a) Orestes and Pylades at the tomb of Agamemnon, on the base of which Electra is kneeling, a phiale in her 1. hand and her r. on top of a hydria; aboveŠbusts of two Furies, (b) nude youth with strigil and stick between draped youth (A 1) and draped woman, each with spray. Neck: (a) Siren, holding fillet and tambourine, (b) female head in profile to 1')
    print(p.get_shape())
    print(p.get_location())
    print(p.get_dimension())
    print(p.get_plate())
    print(p.get_extras())
    print(p.get_description())
