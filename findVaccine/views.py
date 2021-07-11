from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import *
import requests,json,time
from datetime import datetime
import random
# Create your views here.
def loginCHeck(request):
    try:
        if request.session.get("mobile"):
            return True
    except KeyError:
        return False

def index(request):
    if loginCHeck(request) == True:
        return redirect(dashboard)

    if request.method=="POST":
        form = loginForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data["otp"]
            if int(otp) == int(request.session["otp"]):
                request.session["name"] = form.cleaned_data["name"]
                request.session["mobile"] = form.cleaned_data["mobile"]
                return redirect(dashboard)
            else:
                form._errors['otp'] = form.error_class([
                    'Invalid Otp'])
                return render(request, "findVaccine/index.html",{'form':form})

    else:
        form = loginForm()
    return render(request, "findVaccine/index.html",{'form':form})

def generateOtpApi(request):
    mobile = int(request.GET.get('mobile'))
    otp = random.randrange(1000,9999)
    request.session["otp"] = otp
    print(otp)
    return HttpResponse(otp)

def dashboard(request):
    return  render(request, 'findVaccine/dash.html',{"name":request.session.get("name")})

def byPincode(request):
    if request.method == "POST":
        pincode = request.POST.get('pincode')
        date = request.POST.get("date")
        age = request.POST.get("age")
        print(age)
        date = datetime.strptime(date, "%Y-%m-%d").strftime('%d-%m-%Y')

        URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(pincode, date)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

        result = requests.get(URL, headers=header)
        response_json = result.json()
        data = response_json["sessions"]
            #data = json.dumps(data, sort_keys=True, indent=4)
        return render(request, 'findVaccine/dash.html', {'data': data,'age':int(age),'pincode':pincode,'date':date,'name':request.session.get("name")})
    return redirect(dashboard)

def logout(request):
    try:
        del request.session["name"]
        del request.session["mobile"]
        del request.session["otp"]
    except KeyError:
        pass
    return redirect(index)