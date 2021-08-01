from django.shortcuts import render, redirect
from .forms import PatientForm, SheetForm, ChartForm
from .models import PatientFile, ClientSheet, ObservationChart
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from . decorators import allow_users
from django.contrib.auth.decorators import login_required

# Create your views here.


def patientfile(request):

    if request.method != 'POST':
        form = PatientForm()

    else:
        form = PatientForm(data=request.POST)
        if form.is_valid():
            print('aliyu')
            form.save()
            

            
            return redirect('/')
        else:
            print('bilya')  

    context = {'form': form}
    
    return render(request, 'patientsrecords/patientfile.html', context )


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'doctor', 'nurse'])  
def patientinfos(request):

    patientfiles = PatientFile.objects.all()
    context = {'patientfiles': patientfiles}

    return render(request, 'patientsrecords/files.html', context)


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'doctor', 'nurse'])
def patient_sheet(request, p_id):
    patientfile = PatientFile.objects.get(id=p_id)
    sheets = patientfile.clientsheet_set.order_by('-updated')
    charts = patientfile.observationchart_set.order_by('-updated')

    context = {'patientfile': patientfile, 'sheets': sheets, 'charts': charts}

    return render(request, 'patientsrecords/p_file1.html', context)


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'doctor', 'nurse'])
def patient_chart(request, p_id):
    patientfile = PatientFile.objects.get(id=p_id)
    sheets = patientfile.clientsheet_set.order_by('-updated')
    charts = patientfile.observationchart_set.order_by('-updated')

    context = {'patientfile': patientfile, 'sheets': sheets, 'charts': charts}

    return render(request, 'patientsrecords/p_file2.html', context)


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['doctor','admin'])
def add_sheet(request, p_id):

    patientfile = PatientFile.objects.get(id=p_id)

    if request.method != 'POST':
        form = SheetForm()

    else:
        form = SheetForm(data=request.POST)
        if form.is_valid():
            print('aliyu')
            new_sheet = form.save(commit=False)
            new_sheet.patientfile = patientfile
            new_sheet.save()
            

            
            return redirect('patientsrecords:patient_sheet', p_id=p_id)
        else:
            print('bilya')  

    context = {'form': form, 'patientfile': patientfile}
    
    return render(request, 'patientsrecords/add_sheet.html', context )

@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['doctor'])
def edit_sheet(request, p_id):
    
    sheet = ClientSheet.objects.get(id=p_id)
    patientfile = sheet.patientfile


    
    form = SheetForm(instance=sheet)

    if request.method == 'POST':

        form = SheetForm(instance=sheet, data=request.POST)
        if form.is_valid():
            print('aliyu')
            form.save()
            return redirect('patientsrecords:patient_sheet', p_id=p_id)
        
    context = {'form': form, 'sheet': sheet, 'patientfile': patientfile}

    return render(request, 'patientsrecords/edit_sheet.html', context)


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'nurse', 'doctor'])
def chart_info(request, p_id):
    patientfile = PatientFile.objects.get(id=p_id)
   

    context = {'patientfile': patientfile, 'charts': charts}

    return render(request, 'patientsrecords/p_file.html', context)


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['nurse'])
def add_chart(request, p_id):

    patientfile = PatientFile.objects.get(id=p_id)
    
    if request.method != 'POST':
        form = ChartForm()
    
    else:
        form = ChartForm(data=request.POST)
        if form.is_valid():
            clientchart = form.save(commit=False)
            clientchart.patientfile = patientfile
            clientchart.save()

            return redirect('patientsrecords:patient_chart', p_id=p_id)
        else:
            print('bilya')  

    context = {'form': form, 'patientfile': patientfile}
    
    return render(request, 'patientsrecords/addchart.html', context )




@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['nurse'])
def edit_chart(request, chart_id):
    chart = ObservationChart.objects.get(id=chart_id)
    patientfile.chart = patientfile

    form = ChartForm(instance=chart)

    if request.method == 'POST':
        form = ChartForm(instance=chart, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('patientsrecords:patient_chart', chart_id=chart_id) 

    context = {'form': form, 'chart': chart}

    return render(request, 'patientsrecords/edit_chart.html', context)