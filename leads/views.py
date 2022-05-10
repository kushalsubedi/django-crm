
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import lead,Agent
from .forms import LeadModelForm,LeadForm
# Create your views here.
  
def home_page(request):
    leads = lead.objects.all()
    content ={
       "leads":leads
    }

    return render (request,"leads/firstpage.html",content)

def lead_detail(request,pk):
    leads= lead.objects.get(id=pk)
    content ={
        "lead":leads
    }
    return render(request,"leads/lead_detail.html",content)

#def lead_create(request):
#    form=LeadForm()
#    if request.method == 'POST':
#        form=LeadForm(request.POST)
#        if form.is_valid():
#            first_name = form.cleaned_data['first_name']
#            last_name=form.cleaned_data['last_name']
#            age=form.cleaned_data['age']
#            agent=Agent.objects.first()
#            lead.objects.create(
#                first_name=first_name,
#                last_name=last_name,
#                age=age,
#                agent=agent,
#            )
#            print("lead has been created ")
#            return redirect('/leads')
#
#

#    context ={
#        "form":LeadForm
#    }
#    return render(request,"create.html",context)

##modelbased forms
def lead_create(request):

    form=LeadModelForm()
    if request.method =='POST':
        form=LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form":form
    }

    return render(request,"leads/create.html",context)

def lead_update(request,pk):
    leads=lead.objects.get(id=pk)
    
    form=LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=leads.cleaned_data())
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        'form':form,
        'lead':leads
    }
    return render(request,'leads/update.html',context)



def lead_delete (request,pk):
    leads=lead.objects.get(id=pk)
    leads.delete()
    return redirect("/leads")