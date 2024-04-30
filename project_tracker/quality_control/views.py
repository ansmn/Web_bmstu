from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import BugReport, FeatureRequest
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'quality_control/index.html')

def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})

def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

from .forms import BugReportForm

def bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

from .forms import FeatureRequestForm

def feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


#Class-Based Views

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')
    
class BugReportListView(ListView):
    model = BugReport
    context_object_name='bugs_list'
    template_name = 'quality_control/bugs_list.html'
    
class FeatureRequestListView(ListView):
    model = FeatureRequest
    context_object_name='features_list'
    template_name = 'quality_control/features_list.html'
    
class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name='bug'
    template_name = 'quality_control/bug_detail.html'
    
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name='feature'
    template_name = 'quality_control/feature_detail.html'