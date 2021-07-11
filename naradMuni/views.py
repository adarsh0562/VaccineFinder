from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
import datetime,time
from newsapi import NewsApiClient
from datetime import date, timedelta

# Create your views here.
def loginPage(request):
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data["username"]
            pwd = form.cleaned_data["password"]
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request,user)
                return redirect(dash)
    else:
        form = LoginForm(label_suffix='')
    return render(request,'naradMuni/login.html',{'form':form})

def signUpPage(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("SIGN UP SUSSESSFULLY")
    else:
        form = SignUpForm(label_suffix='')
    return render(request,'naradMuni/signup.html',{'form':form})

def dash(request):
    if request.user.is_authenticated:
        return redirect(getNews)
    else:
        form = LoginForm(label_suffix='')
        return render(request,'naradMuni/login.html',{'form':form,'error_messgages':"Session Expired!! \n Login Again"})


def logoutPage(request):
    logout(request)
    return redirect(loginPage)

def getNews(request):
    dt = datetime.date.today()
    day = dt.strftime("%A, %B %d, %Y")
    keyword = "india"
    newsapi = NewsApiClient(api_key='d09c32eb260a43fcb5ab6bf6a6fdb3b0')
    all_articles = newsapi.get_everything(q='{}'.format(keyword),
                                          from_param='{}'.format(date.today() - timedelta(1)),
                                          to='{}'.format(date.today()),
                                          language='en',
                                          sort_by='relevancy',
                                          page=2)

    top_headlines = newsapi.get_top_headlines(q='{}'.format(keyword),
                                              category='general',
                                              language='en',
                                              country='in')
    BigHeadLine = newsapi.get_top_headlines(q='{}'.format(keyword),
                                            category='health',
                                            language='en',
                                            country='in')
    businessNews = newsapi.get_top_headlines(q='{}'.format(keyword),
                                             category='business',
                                             language='en',
                                             country='in')
    technologyNews = newsapi.get_top_headlines(q='{}'.format(keyword),
                                               category='technology',
                                               language='en',
                                               country='in')
    entertainmentNews = newsapi.get_top_headlines(q='{}'.format(keyword),
                                                  category='entertainment',
                                                  language='en',
                                                  country='in')
    sportsNews = newsapi.get_top_headlines(q='{}'.format(keyword),
                                           category='sports',
                                           language='en',
                                           country='in')

    # /v2/sources
    sources = newsapi.get_sources()

    return render(request, 'naradMuni/dashboard.html',
                  {'day': day, 'articles': all_articles, 'headLines': top_headlines, "bigHeadline": BigHeadLine,
                   "businessNews": businessNews, "technologyNews": technologyNews,
                   "entertainmentNews": entertainmentNews, "sportsNews": sportsNews,'name': request.user})


def contactusPage(request):
    if request.user.is_authenticated:
        dt = datetime.date.today()
        day = dt.strftime("%A, %B %d, %Y")
        keyword = "india"
        newsapi = NewsApiClient(api_key='d09c32eb260a43fcb5ab6bf6a6fdb3b0')
        top_headlines = newsapi.get_top_headlines(q='{}'.format(keyword),
                                                  category='general',
                                                  language='en',
                                                  country='in')
        # /v2/sources
        sources = newsapi.get_sources()
        return render(request, 'naradMuni/contactus.html',{'day': day,'headLines': top_headlines,'name': request.user})
    else:
        form = LoginForm(label_suffix='')
    return render(request,'naradMuni/login.html',{'form':form,'error_messgages':"Session Expired!! \n Login Again"})
