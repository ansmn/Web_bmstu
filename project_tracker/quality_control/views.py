from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import BugReport, FeatureRequest

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> {bug.status}</li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a> {feature.status}</li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h3>Детали бага {bug_id}</h3>'
    response_html += f'title:{bug.title}<br>'
    response_html += f'description:{bug.description}<br>'
    response_html += f'project:{bug.project}<br>'
    response_html += f'task:{bug.task}<br>'
    response_html += f'status:{bug.status}<br>'
    response_html += f'priotity:{bug.priority}<br>'
    return HttpResponse(response_html)

def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h3>Детали улучшения {feature_id}</h3>'
    response_html += f'title:{feature.title}<br>'
    response_html += f'description:{feature.description}<br>'
    response_html += f'project:{feature.project}<br>'
    response_html += f'task:{feature.task}<br>'
    response_html += f'status:{feature.status}<br>'
    response_html += f'priotity:{feature.priority}<br>'
    return HttpResponse(response_html)

#Class-Based Views

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        features_list_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{features_list_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)
    
class BugReportListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
        for bug in bugs:
            bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> {bug.status}</li>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)
    
class FeatureRequestListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список запросов на улучшение</h1><ul>'
        for feature in features:
            features_html += f'<li><a href="{feature.id}/">{feature.title}</a> {feature.status}</li>'
        features_html += '</ul>'
        return HttpResponse(features_html)
    
class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f'<h3>Детали бага {bug.id}</h3>'
        response_html += f'title:{bug.title}<br>'
        response_html += f'description:{bug.description}<br>'
        response_html += f'project:{bug.project}<br>'
        response_html += f'task:{bug.task}<br>'
        response_html += f'status:{bug.status}<br>'
        response_html += f'priotity:{bug.priority}<br>'
        return HttpResponse(response_html)
    
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h3>Детали улучшения {feature.id}</h3>'
        response_html += f'title:{feature.title}<br>'
        response_html += f'description:{feature.description}<br>'
        response_html += f'project:{feature.project}<br>'
        response_html += f'task:{feature.task}<br>'
        response_html += f'status:{feature.status}<br>'
        response_html += f'priotity:{feature.priority}<br>'
        return HttpResponse(response_html)