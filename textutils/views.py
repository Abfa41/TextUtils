# I created this file
from django.http import HttpResponse
import re
from django.shortcuts import render

def home(req):
    params = {"name": "Bharat Sir","words":0,"lines":0,"message":"Welcome to TextUtils 😊 !!!"}
    return render(req,"index.html",params)
    # return HttpResponse("Hello world")

def about(req):
    
    return render(req,"about.html")
    # return HttpResponse("Hello world")

def lower(req):
    if req.method=="POST":
        text = req.POST.get("text","")
        text = text.lower()
        params={"text": text,"message": "Text converted to Lower case Successfully!!!"}
        return render(req,"index.html",params)

def upper(req):
    if req.method=="POST":
        text = req.POST.get("text","")
        text = text.upper()
        params={"text": text,"message": "Text converted to Upper case Successfully!!!"}
        return render(req,"index.html",params)

def clear(req):
    if req.method=="POST":
        params={"text": "","message":"Text cleared..."}
        
        return render(req,"index.html",params)
    
def trim(req):
    if req.method=="POST":
        t = normalize_spaces(req.POST.get("text",""))
        return render(req,"index.html",{"text": t,"message":"Text trimmed Successfully!!"})
    
def analyze(req):
    text = req.POST.get("text","")
    params = {"text": text,"name": "Bharat Sir","words": calcWords(text),"lines": calcLines(text),"message": "Text Analyzed Successfully 👍 !!!"}
    return render(req,"index.html",params)






# custom functions

def normalize_spaces(input_string):
    # Replace multiple spaces (including tabs, newlines, etc.) with a single space
    normalized_string = re.sub(r'\s+', ' ', input_string)

    # Strip leading and trailing spaces
    normalized_string = normalized_string.strip()

    return normalized_string

def calcWords(text):
    return len(text.split(" "))

def calcLines(text):
    return len(text.split("."))
    