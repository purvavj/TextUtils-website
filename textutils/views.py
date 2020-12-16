# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html') #render takes 2 argument 1 is must
    
    '''return HttpResponse("""<h1>Hello, choose:</h1> 
    <br><a href="http://127.0.0.1:8000/removepunc">Removepunc</a> <br>
    <a href="http://127.0.0.1:8000/capfirst">Capfirst</a>
    <br><a href="http://127.0.0.1:8000/newlineremover">Newlineremover</a>
    <br> <a href="http://127.0.0.1:8000/spaceremover">Spaceremover</a>
    <br> <a href="http://127.0.0.1:8000/charcount">Charcount</a>""")'''

def analyze(request):
    #get the text
    djtext=request.POST.get('text', 'default') #jo name button ko diya hai jiski value text h
    rpunc=request.POST.get('removepunc', 'off') #jo name button ko diya hai uski info,
                    #dusra parimeter is default value jo bhi deni ho
    cap=request.POST.get('capatlise', 'off')
    ccount= request.POST.get("charcount", "off")
    #print(rpunc)
    #print(djtext)
    punc= ''' '!@#$%^&*()_,.;/\?<>:"[]{} '''
    analyzed = ""
    if rpunc == "on":
        for i in djtext:
            if i not in punc:
                analyzed = analyzed + i
        djtext = analyzed
         
        #params= {"purpose":djtext, "analyzed_text":analyzed} #dictionary
        #analyze text
        #render(request, 'analyzer.html', params)
    
    if cap == "on":
        analyzed = djtext.upper()  
        
    if ccount =="on":
        count = 0
        for i in djtext:
            if i.isalpha():
                count += 1
            else: continue
        analyzed = analyzed + "\n" + "the count is"+ str(count) 
    
    if analyzed != "":
        param= {"purpose": "Analysis is here", "analyzed_text": analyzed}
        return render(request, "analyzer.html", param)
    else:
        return HttpResponse("Error")

"""
def capfirst(request):
    return HttpResponse('Capfirst <br> <a href="/">back</a>')

def newlineremover(request):
    return HttpResponse('newlineremover <br> <a href="/">back</a>')

def spaceremover(request):
    return HttpResponse('spaceremover <br> <a href="/">back</a>')

def charcount(request):
    return HttpResponse('charcount<br> <a href="/">back</a>')"""