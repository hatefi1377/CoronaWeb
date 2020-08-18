from django.shortcuts import render
from .models import CaseDetail
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


def home (request):
    case = CaseDetail.objects.all()
    context={
        'cases':case
    }
    return render (request,'home.html',context)

#class CaseListView(ListView):
#    model = CaseDetail
#    template_name = 'home.html'
#    context_object_name = 'case'
#    ordering = ['-date_entered']

class CaseDetailView(DetailView):
    model = CaseDetail
    template_name = 'casedetail.html'
    context_object_name = 'case'

class CaseCreateView(LoginRequiredMixin , CreateView) :
    model = CaseDetail
    fields = ['case_name' , 'case_number','case_address','case_last_seen','case_last_seen_date'
    ,'case_image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CaseUpdateView(LoginRequiredMixin ,UserPassesTestMixin , UpdateView) :
    model = CaseDetail
    fields = ['case_name' , 'case_number','case_address','case_last_seen','case_last_seen_date'
    ,'case_image']

    def test_func(self):
        case = self.get_object()
        if self.request.user == case.user:
            return True
        return False

class CaseDeleteView(LoginRequiredMixin ,UserPassesTestMixin , DeleteView):
    model = CaseDetail
    success_url = '/'
    def test_func(self):
        case = self.get_object()
        if self.request.user == case.user:
            return True
        return False
