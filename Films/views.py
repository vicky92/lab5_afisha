# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from Films.models import *
import datetime
from django.core.context_processors import csrf

# searching by the time

def GetMain(request):
    return render_to_response('index.html', {})

def GetAllSession(request):
    if request.method == 'POST':
        return GetSession(request)
    obj = Poster.objects.all()
    c =  {'selected' : obj}

    c.update(csrf(request))  
    return render_to_response('selectsession.html',c)

def GetCinemaInfo(request,ID):
   # ID =  int(ID)
    obj = Cinema.objects.get(pk=ID)
    c ={'selected' : obj}
    return render_to_response('aboutcinema.html',c)

def GetFilmInfo(request,ID):
   # ID =  int(ID)
    obj = Film.objects.get(pk=ID)
    c ={'selected' : obj}
    return render_to_response('aboutfilm.html',c)

def GetSessionInfo(request,ID):
   # ID =  int(ID)
    obj = Poster.objects.get(pk=ID)
    c ={'selected' : obj}
    return render_to_response('aboutsession.html',c)
        
def GetSession(request):
    c = {}
    try:
        timeSt =   datetime.datetime(int(request.POST["yearSt"]), 
                              int(request.POST["monthSt"]), int(request.POST["daySt"]), int(request.POST["hourSt"]),
                              int(request.POST["minuteSt"]))
        timeEnd =  datetime.datetime(int(request.POST["yearEnd"]), 
                              int(request.POST["monthEnd"]), int(request.POST["dayEnd"]), int(request.POST["hourEnd"]),
                              int(request.POST["minuteEnd"]))
        obj = Poster.objects.filter(viewDate__gt=timeSt, viewDate__lt=timeEnd)
        c ={'selected' : obj}
    except:
        pass   
   
    c.update(csrf(request))    
    return render_to_response('selectsession.html',c)


# searching by the film

def GetAllFilm(request):
    if request.method == 'POST':
        return GetFilm(request)
    obj = Film.objects.all()
    c = {'selected' : obj}
    c.update(csrf(request))  
    return render_to_response('selectfilm.html', c)

def GetFilm(request):
    c= {}
    try:
        filmName = request.POST["name"]
        obj = Film.objects.filter(name=filmName)
        c = {'selected' : obj}
    except:
        pass
    c.update(csrf(request))
    return render_to_response('selectfilm.html', c)
 
def GetAllCinema(request):
    if request.method == 'POST':
        return GetCinema(request)
    obj = Cinema.objects.all()

    c = {'selected' : obj}
    c.update(csrf(request))
    return render_to_response('selectcinema.html', c)

def GetCinema(request):
    c = {}
    try:
        cinemaName =  request.POST["name"]
        obj = Cinema.objects.filter(name=cinemaName)
        c = {'selected' : obj}
    except:
        pass
    c.update(csrf(request))
    return render_to_response('selectcinema.html', c)

def UpdateSession(request, ID):
   # ID =  int(ID)
    obj = Poster.objects.get(pk=ID)
    if request.method == 'POST':
        try:
            fID =Film.objects.get(pk=request.POST["fID"])
            cID = Cinema.objects.get(pk=request.POST["cID"])
            
            t = datetime.datetime(int(request.POST["year"]), 
                                  int(request.POST["month"]), int(request.POST["day"]), int(request.POST["hour"]),
                                  int(request.POST["minute"]))
            obj.viewDate = t
            obj.cinemaID = cID
            
            obj.filmID = fID
            obj.save()
        except:
            return  render_to_response('decline.html',{})
        return  render_to_response('accept.html',{})
    elif request.method == 'GET':
        cinema = Cinema.objects.all()
        film   = Film.objects.all()
        c = {'cinema':cinema, 'film':film, 'session':obj}
        
        c.update(csrf(request))
        return  render_to_response('updatesession.html',c)

def UpdateFilm(request, ID):
   # ID =  int(ID)
    obj = Film.objects.get(pk=ID)
    if request.method == 'POST':
        try:
            #ID = int(ID)
            filmName = request.POST["name"]
            about = request.POST["about"]
            obj = Film.objects.get(pk=ID)
            obj.name = filmName
            obj.about = about
            obj.save()
        except Exception as e:
            print e
            return  render_to_response('decline.html',{})
        return  render_to_response('accept.html',{})
    elif request.method == 'GET':
        c = {'film':obj}
        
        c.update(csrf(request))
        return  render_to_response('updatefilm.html',c)

def UpdateCinema(request, ID):
   # ID =  int(ID)
    obj = Cinema.objects.get(pk=ID)
    if request.method == 'POST':
        try:
            #ID = int(ID)
            cinemaName = request.POST["name"]
            address = request.POST["address"]
            obj.name = cinemaName
            obj.address = address
            obj.save()
        except:
            return  render_to_response('decline.html',{})
        return  render_to_response('accept.html',{})
    elif request.method == 'GET':
        c = {'cinema':obj}
        
        c.update(csrf(request))
        return  render_to_response('updatecinema.html',c)

def CreateSession(request):
    if request.method == 'POST':
        try:
           # print request.POST["fID"], type(request.POST["fID"]), type(Film.pk) 
           # fID = Film.objects.filter(pk=request.POST["fID"])
           # fID= get_object_or_404(Film, pk=equest.POST["fID"]))
            fID =  Film.objects.get(pk=request.POST["fID"])
            cID = Cinema.objects.get(pk= request.POST["cID"])
            t = datetime.datetime(int(request.POST["year"]), 
                                  int(request.POST["month"]), int(request.POST["day"]), int(request.POST["hour"]),
                                  int(request.POST["minute"]))
            Poster(viewDate=t, filmId = fID, cinemaId = cID).save()
        except Exception as e:
            print  e
            return  render_to_response('decline.html',{})
        return  render_to_response('accept.html',{})
    elif request.method == 'GET':
        cinema = Cinema.objects.all()
        film   = Film.objects.all()
        c = {'cinema':cinema, 'film':film}
        
        c.update(csrf(request))
        return  render_to_response('addsession.html',c)

def CreateFilm(request):
    if request.method == 'POST':
        try:
            filmName = request.POST["name"]
            aboutFilm = request.POST["about"]
            Film(name=filmName, about = aboutFilm).save()

        except:
            return  render_to_response('decline.html',{})
        return  render_to_response('accept.html',{})
    elif request.method == 'GET':
        c = {}
        
        c.update(csrf(request))
        return  render_to_response('addfilm.html',c)

def CreateCinema(request):
    if request.method == 'POST':
        try:
            cinemaName = request.POST["name"]
            addressCinema = request.POST["address"]
            Cinema(name=cinemaName, address = addressCinema).save()
           # print type(a.pk), a.pk
        except Exception as e:
            print e
            return  render_to_response('decline.html',{})
        return  render_to_response('accept.html',{})
    elif request.method == 'GET':
        c = {}
        
        c.update(csrf(request))
        return  render_to_response('addcinema.html',c)
    
def DeleteSession(request, ID):
    try:
      #  ID = int(ID)
        Poster.objects.get(pk = ID).delete()
    except:
        return  render_to_response('decline.html',{})
    return  render_to_response('accept.html',{})

def DeleteFilm(request, ID):
    try:
       # ID = int(ID)
        Film.objects.get(pk=ID).delete()
    except:
        return  render_to_response('decline.html',{})
    return  render_to_response('accept.html',{})
def DeleteCinema(request, ID):
    try:
      #  ID = int(ID)
        Cinema.objects.get(pk=ID).delete()
    except:
        return  render_to_response('decline.html',{})
    return  render_to_response('accept.html',{})
