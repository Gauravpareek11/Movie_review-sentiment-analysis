from django.http import HttpResponse
from django.shortcuts import render
from keras.models import load_model
def home(request):
    return render(request,"home.html")
def result(request):
    model=load_model('review')
    text=request.GET['Review']
    print(text)
    ans=model.predict([text])
    if(ans[0][0]>0.50):
        pre="Positive Review"
    else:
        pre="Negative Review"
    return render(request,"result.html",{'ans':ans[0][0],'pre':pre})