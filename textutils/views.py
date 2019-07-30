#this file is created by me-karishma gupta
from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    return render(request,'index.html')


def ex1(request):
      s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
      return HttpResponse(s)
def analyze(request):
    djText=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    NewLineRemover=request.POST.get('NewLineRemover','off')
    ExtraSpaceRemover=request.POST.get('ExtraSpaceRemover','off')


    if removepunc=='on':

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djText:
            if char not in punctuations:
                analyzed=analyzed + char

        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djText=analyzed

    if(fullcaps=="on"):
        analyzed=""
        for char in djText:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to UpperCase','analyzed_text':analyzed}
        djText=analyzed

    if(NewLineRemover=="on"):
        analyzed=""
        for char in djText:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        djText=analyzed


    if(ExtraSpaceRemover=="on"):
        analyzed=""
        for index,char in enumerate(djText):
            if not(djText[index]==' ' and djText[index+1]==' '):
                analyzed=analyzed+char
        params={'purpose':'Extra Space Remover','analyzed_text':analyzed}
    if(removepunc!="on" and ExtraSpaceRemover!="on" and NewLineRemover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")


    return render(request,'analyze.html',params)
