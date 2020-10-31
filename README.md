# Mediterranean-Archaeology
PDF extraction and database development - Final year project-LaTrobe

## PDF Extraction Server

A method to automate the extraction process . 

Steps:

Read a PDF file, scan the data to identify Vase details(THE RED-FIGURED VASES OF PAESTUM )
Return a Json Object 


Examples: 
  ```
  path : '/'
  return : 
  "Vase_details": [
    {
      "description": " (a) Orestes and Pylades at the tomb of Agamemnon, on the base of which Electra is kneeling, a phiale in her 1. hand and her r. on top of a hydria; above-busts of two Furies, (b) nude youth with strigil and stick between draped youth (A 1) and draped woman, each with spray. Neck: (a) Siren, holding fillet and tambourine, (b) female head in profile to 1",
      "dimension": "Ht. 42-3. ",
      "extras": "Chamay, La Guerre de Troie, pp. 24-5, ill. on p. 25; Genava 33, 1985, p. 185, fig. 1; Le Peinlre de Darius et son milieu ( 1986), pp. 264-9, with colour ill. on p. 29; detail, Musees de Geneve 265, May 1986, p. 17.",
      "id": 1,
      "location": "Geneva HR 29",
      "plate": "PLATE 15",
      "shape": "Neck-amphora "
    },
    {
      "description": "Upper part of woman, with basket upon her head, clasping the shaft of an Ionic column (from a funerary monument) with her r. hand",
      "dimension": ". 9-6 x 11-95.",
      "extras": null,
      "id": 2,
      "location": "New York 1985.74",
      "plate": "PLATE 16 a",
      "shape": "Fragment (of a neck-amphora) "
    },
  ```
  ## Installing Dependencies
  
  pip install -r requirements.txt
  
## Running Server
export FLASK_APP=app.py
export FLASK_ENV=development
flask run


## Files Details 

Main Files: 
app.py -> Server 
Paragraph.py -> create a paragraph object 
Pdf_extractor.py -> create an instance of pdf extraction process.
newRvp3.pdf -> input pdffile for extraction

Additonal Files in the folder are meant for testing purposes.





