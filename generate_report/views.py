from django.shortcuts import render, redirect
from .models import LiverFunctionTest, RenalFunctionTest, BloodGlucose
from django.conf import settings
from django.template.loader import render_to_string, get_template
from django.http import HttpResponse
from weasyprint import HTML, CSS
import weasyprint
from weasyprint.fonts import FontConfiguration
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import BloodGlucoseForm, RenalFunctionTestForm, LiverFunctionTestForm
from patientsrecords.models import PatientFile


# Create your views here.

def bloodGlucoseTest(request):
    if request.method == 'POST':
        form = BloodGlucoseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BloodGlucoseForm()
    context = {'form': form}
    return render(request, 'generate_report/addtest.html', context)


def edit_test(request, mc):
    
 
    blood_glucose = BloodGlucose.objects.get(id=mc)


    
    form = BloodGlucoseForm(instance=blood_glucose)

    if request.method == 'POST':

        form = BloodGlucoseForm(instance=blood_glucose, data=request.POST)
        if form.is_valid():
            print('aliyu')
            form.save()
            return redirect('generate_report:record', mc=mc)
        
    context = {'form': form}

    return render(request, 'generate_report/addtest.html', context)


def renalTest(request):
    if request.method == 'POST':
        form = RenalFunctionTestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RenalFunctionTestForm()
    context = {'form': form}
    return render(request, 'generate_report/addtest.html', context)


def liverTest(request):
    if request.method == 'POST':
        form = LiverFunctionTestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = LiverFunctionTestForm()
    context = {'form': form}
    return render(request, 'generate_report/addtest.html', context)


@login_required(login_url = '/account/login/')
def view_report(request):
    liver = LiverFunctionTest.objects.all()
    renal = RenalFunctionTest.objects.all()
    blood = BloodGlucose.objects.all()

    context = {'liver': liver, 'renal': renal, 'blood': blood}

    return render(request, 'generate_report/report.html', context)


@login_required(login_url = '/account/login/')
def download_report(request, my_id):

    user = User.objects.get(id=my_id)
    #user.id = my_id
    
    liver = LiverFunctionTest.objects.all()
    renal = RenalFunctionTest.objects.all()
    
    blood = BloodGlucose.objects.all()
   
    context = {'liver': liver, 'renal': renal, 'blood': blood}
    
    html = render_to_string('generate_report/report_pdf.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="medical_report.pdf"'
    stylesheets=[CSS('static/css/bootstrap.min.css')]
    weasyprint.HTML(string=html).write_pdf(response, stylesheets, presentational_hints=True)
    return response
    

def patientFilterView(request):
    patientFile = PatientFile.objects.all()
    username_exact_query = request.GET.get('username')
    

    if username_exact_query != '' and username_exact_query is not None:
        #patientFile.filter(department__icontains=username_exact_query)
        patientFile = patientFile.filter(phone__iexact=username_exact_query)
        print(username_exact_query)
        
        
    context = {'patientFiles': patientFile}

    return render(request, 'generate_report/searchform.html', context)


def record(request, p_id):
    qs = PatientFile.objects.get(id=p_id)

    clientsheets = qs.clientsheet_set.all()

    context = {'queryset': qs, 'clientsheets':clientsheets}
    return render(request, 'patientsrecords/records.html', context)
