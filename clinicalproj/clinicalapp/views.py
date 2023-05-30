from django.shortcuts import render,redirect
from clinicalapp.models import Patient,ClinicalData
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from clinicalapp.forms import ClinicalDataForm

# Create your views here.
def addData(request,**kwargs):
   form =ClinicalDataForm()
   patient=Patient.objects.get(id=kwargs=['pk'])
   if request.method=='POST':
       form=ClinicalDataForm(request.POST)
       if form.is_valid():
           form.save()
        return redirect('/')   
           
   return render(request,'clinicalapp/clinicaldata_form.html',{'form':form, 'patient':patient})

class PatientListView(ListView):
    model=Patient


class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','lastname','age')

class PatientUpdateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index') #goback to index.html
    fields=('firstname','lastname','age')
 
class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','lastname','age')
 
