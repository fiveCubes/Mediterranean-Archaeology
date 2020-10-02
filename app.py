from flask import Flask,jsonify
from Pdf_extractor import pdf_extractor

app=Flask(__name__)

@app.route('/')
def index():
    pdf_ex = pdf_extractor('./newRvp3.pdf')
    p_list= [p.get_attributes() for p in pdf_ex.get_paragraphs()]
    return jsonify({"success": True , "Vase_details":p_list})


