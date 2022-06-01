from curses.ascii import US
from django.core.mail import send_mail

from django.views import generic
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import lead,Agent
from .forms import LeadModelForm,CustomUserCreationForm
# Create your views here.
#
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DetailView,DeleteView
#
#class based views 

class SignupView(generic.CreateView):
    template_name='registration/signup.html'
    from_class =CustomUserCreationForm
  

    def get_succedd_url(self)->str:
        return reverse("login")



class LandingPageView(generic.TemplateView):
    template_name="landingpage.html"


class LeadListView(generic.ListView):
    template_name="leads/leadlist.html"
    queryset = lead.objects.all()     
    #context_objext_name='leads'


class LeadDetailView(generic.DetailView):
    template_name="leads/lead_detail.html"
    queryset = lead.objects.all()
    context_objext_name='lead'

class LeadCreateView(generic.CreateView):
    template_name="leads/create.html"
    form_class=LeadModelForm

    def get_success_url(self) -> str:
        return reverse("lead:lead-list")

    def form_valid(self,form):
        send_mail (
            subject="A lead has been created",
            message =" Go to the sitr to see the new lead",
            from_email = "test@test.com",
            recipient_list = ['test2@test.com']
        )
        return super(LeadCreateView,self).form_valid(form)


class LeadUpdateView(generic.UpdateView):
    model=lead
    template_name="leads/update.html"
    form_class=LeadModelForm

    def get_success_url(self) -> str:
         return reverse("lead:lead-list")

class LeadDeleteView(generic.DeleteView):
    template_name="leads/lead_delete.html"
    model=lead

    def get_success_url(self) -> str:
        return reverse("lead:lead-list")
        
    
 
#method based views
def landing_page(request):
    return render(request,"landingpage.html") 

def lead_list(request):
    leads = lead.objects.all()
    content ={
       "leads":leads
    }

    return render (request,"leads/leadlist.html",content)

def lead_detail(request,pk):
    leads= lead.objects.get(id=pk)
    content ={
        "lead":leads
    }
    return render(request,"leads/lead_detail.html",content)

""" #def lead_create(request):
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
    """