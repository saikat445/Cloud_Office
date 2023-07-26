from django.shortcuts import render,redirect
from app.models import trialdata, marketsample, market_image, complaint, testsample, test_image, accounts
from django.http import HttpResponse
import csv
#from Office_work.forms import HotelForm
from django.conf.urls.static import static
from app.forms import ImageForm, TestsampleImageForm



def INDEX(request):
    return render(request,'main/index.html')

def Plant_trial(request):
    if request.method == 'POST':
        setno = request.POST.get('setno')
        trialdate = request.POST.get('trialdate')
        batterytype = request.POST.get('batterytype')
        trial_location = request.POST.get('trial_location')
        description = request.POST.get('description')
        receivedate = request.POST.get('receivedate')

        #print(can_weight,can_height,can_wall,can_bottom)
        index = trialdata(
            setno= setno,
            trialdate = trialdate,
            batterytype = batterytype,
            trial_location = trial_location,
            description = description,
            receivedate = receivedate,
        )
        print(setno)
        index.save()
    return render(request,'main/Plant_trial.html')

def Plant_trial_view(request):
    #can_data = trialdata.objects.all().order_by('-date')
    trial_data = trialdata.objects.all()
    context = {
        'trial_data': trial_data
    }
    return render(request, 'main/Plant_trial_view.html',context)

def Trial_data_download(request):
    response = HttpResponse(content_type='text/csv')
    #print(context)
    writer = csv.writer(response)
    writer.writerow(['Set NO','Trial date','battery_type','Trial location','Description','receivedate'])
    for user in trialdata.objects.all().values_list('setno','trialdate','batterytype','trial_location','description','receivedate'):
        writer.writerow(user)

    response['Content-Disposition'] = 'attachment; filename="trial_data.csv"'
    return response

def market_sample(request):
    if request.method == 'POST':
        batterytype = request.POST.get('batterytype')
        name = request.POST.get('name')
        description = request.POST.get('description')
        mfg = request.POST.get('mfg')
        price = request.POST.get('price')
        shelflife = request.POST.get('shelflife')
        receivedate = request.POST.get('receivedate')

        #print(can_weight,can_height,can_wall,can_bottom)
        index2 = marketsample(
            batterytype= batterytype,
            name = name,
            description = description,
            mfg = mfg,
            price = price,
            shelflife = shelflife,
            receivedate = receivedate,
        )
        index2.save()
    return render(request,'main/market_sample.html')

def market_sample_view(request):
    #can_data = trialdata.objects.all().order_by('-date')
    market_sample_data = marketsample.objects.all()
    context = {
        'market_sample_data': market_sample_data
    }
    return render(request, 'main/market_sample_view.html',context)

def market_sample_download(request):
    response = HttpResponse(content_type='text/csv')
    #print(context)
    writer = csv.writer(response)
    writer.writerow(['Battery type','Name','Description','Mfg Date','Price','Shelf life','Receive date'])
    for user in marketsample.objects.all().values_list('batterytype','name','description','mfg','price','shelflife','receivedate'):
        writer.writerow(user)

    response['Content-Disposition'] = 'attachment; filename="market_data.csv"'
    return response

def market_image_upload (request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'main/market_image_upload.html', {'form': form})

def market_image_view (request):
    image_market = market_image.objects.all()
    context = {
        'image_market': image_market
    }
    return render(request, 'main/market_image_view.html', context)

def market_complaint(request):
    if request.method == 'POST':
        complaint_no = request.POST.get('complaint_no')
        complainer = request.POST.get('complainer')
        battery_type = request.POST.get('battery_type')
        description = request.POST.get('description')
        mfg = request.POST.get('mfg')
        status = request.POST.get('status')
        receivedate = request.POST.get('receivedate')

        #print(can_weight,can_height,can_wall,can_bottom)
        index3 = complaint(
            complaint_no = complaint_no,
            complainer  = complainer,
            battery_type = battery_type,
            description = description,
            mfg = mfg,
            status = status,
            receivedate = receivedate,
        )
        index3.save()
        print(complaint_no)
    return render(request,'main/market_complaint.html')

def market_complaint_view(request):
    #can_data = trialdata.objects.all().order_by('-date')
    market_complaint_data = complaint.objects.all()
    context = {
        'market_complaint_data': market_complaint_data
    }
    return render(request, 'main/market_complaint_view.html',context)

def market_complaint_download(request):
    response = HttpResponse(content_type='text/csv')
    #print(context)
    writer = csv.writer(response)
    writer.writerow(['Complaint No','Complainer','Battery type','Description','Mfg','Status','Receive date'])
    for user in complaint.objects.all().values_list('complaint_no','complainer','battery_type','description','mfg','status','receivedate'):
        writer.writerow(user)

    response['Content-Disposition'] = 'attachment; filename="complaint_data.csv"'
    return response

def test_sample(request):
    if request.method == 'POST':
        receivedno = request.POST.get('receivedno')
        samplename = request.POST.get('samplename')
        description = request.POST.get('description')
        mfg = request.POST.get('mfg')
        teststatus = request.POST.get('teststatus')
        receivedate = request.POST.get('receivedate')

        #print(can_weight,can_height,can_wall,can_bottom)
        index3 = testsample(
            receivedno= receivedno,
            samplename = samplename,
            description = description,
            mfg = mfg,
            teststatus = teststatus,
            receivedate = receivedate,
        )
        index3.save()
    return render(request,'main/test_sample.html')

def test_sample_view(request):
    #can_data = trialdata.objects.all().order_by('-date')
    test_sample_data = testsample.objects.all()
    context = {
        'market_sample_data': test_sample_data
    }
    return render(request, 'main/test_sample_view.html',context)

def testsample_image_upload (request):
    if request.method == 'POST':
        form = TestsampleImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('success')
    else:
        form = TestsampleImageForm()
    return render(request, 'main/testsample_image_upload.html', {'form': form})

def testsample_image_view (request):
    test_sample_image = test_image.objects.all()
    context = {
        'test_image': test_sample_image
    }
    return render(request, 'main/testsample_image_view.html', context)

def accounts_data (request):
    if request.method == 'POST':
        po_no = request.POST.get('po_no')
        date = request.POST.get('date')
        suppliername = request.POST.get('suppliername')
        amount = request.POST.get('amount')
        description = request.POST.get('description')

        #print(can_weight,can_height,can_wall,can_bottom)
        index4 = accounts(
            po_no= po_no,
            date = date,
            suppliername = suppliername,
            amount = amount,
            description = description,

        )
        index4.save()
    return render(request,'main/accounts.html')

def accounts_view(request):
    #can_data = trialdata.objects.all().order_by('-date')
    accounts_data = accounts.objects.all()
    context = {
        'accounts_data': accounts_data
    }
    return render(request, 'main/accounts_view.html',context)
