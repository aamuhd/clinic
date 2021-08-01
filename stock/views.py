from django.shortcuts import render, redirect
from .models import Category, Medicine, MedicineGiven
from .forms import *
from patientsrecords.decorators import allow_users
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'pharmacist'])
def categories(request):

    cat = Category.objects.all()

    context = {'categories': cat}

    return render(request, 'stock/categories.html', context)



@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'pharmacist'])
def medicine(request, m_id):
    category = Category.objects.get(id=m_id)
    med = category.medicine_set.all()

    context = {'medicines': med, 'category': category}

    return render(request, 'stock/medicine.html', context)


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'pharmacist'])
def view_medicines(request):
    medicines = Medicine.objects.all()
    context = {'medicines': medicines}

    return render(request, 'stock/medicines.html', context)


def category(request, m_id):
    categories = Category.objects.get(id=m_id)
    medicines = categories.medicine_set.all()
    
    context = {'categories': categories, 'medicines': medicines}

    return render(request, 'stock/category.html', context)


@login_required(login_url = 'account:login')
@allow_users(authorized_users = ['admin', 'pharmacist'])
def add_medicine(request, m_id):
    categories = Category.objects.get(id=m_id)
    

    if request.method != 'POST':
        form = MedicineForm(initial={'category': categories})
    else:
        form = MedicineForm(data=request.POST)
        if form.is_valid():
            #new_medicine = form.save(commit=False)
            #new_medicine.categories = new_medicine
            #new_medicine.save()
            form.save()
            return redirect('stock:medicine', m_id=m_id)

    context = {'form': form, 'categories': categories}

    return render(request, 'stock/add_medicine.html', context)



def medicine_given(request, m_id):

    #categories = Category.objects.get(id=m_id)
    medicines = Medicine.objects.get(id=m_id)
    #medicines.category = categories
    category = medicines.category
    form = MedicineGivenForm(initial={'medicine': medicines})
    
    if request.method == 'POST':
        form = MedicineGivenForm(data=request.POST)
        if form.is_valid():
            m_given = form.save(commit=False)
            m_given.medicine = medicines
            m_given.save()
            return redirect('stock:medicine', category.id)

    context = {'form': form}
    return render(request, 'stock/medicine_given.html', context)


def add_category(request):

    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock:view_medicines')

    context = {'form': form}

    return render(request, 'stock/add_category.html', context)