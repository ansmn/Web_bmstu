from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import BugReport, FeatureRequest

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    features_list_url = reverse('quality_control:features_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{features_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

def features_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<a>Детали бага </a>{bug_id}'
    return HttpResponse(response_html)

def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<a>Детали улучшения </a>{feature_id}'
    return HttpResponse(response_html)