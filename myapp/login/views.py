from django.shortcuts import render, redirect
from . models import Destination,mlmodel,mlmodel1,mlmodel2
import pickle

from sklearn.linear_model import LogisticRegression
# Create your views here.
def result(request):
    if request.method == 'POST':
        username = request.POST['username']
        username = int(username)
        password = request.POST['password']
        objs = mlmodel.objects.all()
        userid = mlmodel.objects.values('USERID_x')
        daydiff = mlmodel.objects.values('DayDiff')
        daydiff1 = mlmodel.objects.values('DayDiff1')
        daydiff2 = mlmodel.objects.values('DayDiff2')
        daydiffMean = mlmodel.objects.values('DayDiffMean')
        daydiffStd = mlmodel.objects.values('DayDiffStd')

        #print(userid[0]['USERID_x'])

        f_lt = []
        lt = []
        for i in range(len(objs)):
            if userid[i]['USERID_x'] == int(username):
                print("Inside")
                lt.append(i)
                lt.append(userid[i]['USERID_x'])
                lt.append(daydiff[i]['DayDiff'])
                lt.append(daydiff1[i]['DayDiff1'])
                lt.append(daydiff2[i]['DayDiff2'])
                lt.append(daydiffMean[i]['DayDiffMean'])
                lt.append(daydiffStd[i]['DayDiffStd'])
                break
        f_lt.append(lt)
        loaded_model = pickle.load(open('C:/Users/Tmuth/Desktop/Project/myapp/login/finalized_model.sav', 'rb'))
        result = loaded_model.predict(f_lt)
        print(result)
        if result == 2:
            result,rresult = '0-1',1
        elif result == 1:
            result,rresult = '2-4',2
        else:
            result,rresult = '5-7',3

        objs1 = mlmodel1.objects.all()
        userid1 = mlmodel1.objects.values('userid')
        date = mlmodel1.objects.values('date')
        rqid = mlmodel1.objects.values('rqid')
        pth = mlmodel1.objects.values('pth')
        values = mlmodel1.objects.values('values')
        print(len(objs1))

        objs2 = mlmodel2.objects.all()
        userid2 = mlmodel2.objects.values('userid')
        date1 = mlmodel2.objects.values('date')
        rqid1 = mlmodel2.objects.values('rqid')
        path_count = mlmodel2.objects.values('pth_count')


        rid = []
        for i in range(len(objs2)):
            if userid2[i]['userid'] == username:
                rid.append(rqid1[i]['rqid'])
        # start = 0
        # frid=[]
        # for i in range(len(rid)):
        #     if rid[i]!=start:
        #         frid.append(rid[i])
        #         start = rid[i]
        print("loop completed")


        return render(request, "login_result.html", {'dests': objs,'pred_date': result,'dest1': objs1,'fresult': rid})

        #return render(request, "login_result.html", {'username': username, 'password': password})
        #return redirect('/')
def signin(request):
    return render(request, "signin.html")

def signup(request):
    return render(request,"signup.html")
