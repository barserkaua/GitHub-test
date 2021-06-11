from django.shortcuts import render, HttpResponse
import requests


def home(request):
    return render(request, 'home.html')


def github(request):
    url = {}
    url_repos = {}
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        url_repos = 'https://api.github.com/users/%s/repos' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
    data = {
        'search_result': search_result,
        'url': url,
        'url_repos': url_repos,
    }

    return render(request, 'github.html', data)
