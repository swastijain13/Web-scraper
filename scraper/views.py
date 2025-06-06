from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from .models import Anchors

# Create your views here.

def fetch_html(request):
    context = {}
    if request.method == "POST":
        action = request.POST.get('action')
        context = {}
        if action == 'fetch':
            url = request.POST.get("url")
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                # response.raise_for_status()

                for a in soup.find_all('a'):
                    href = a.get("href")
                    name = a.get_text(strip=True)   

                    if href:
                        Anchors.objects.create(
                            href = href,
                            name = name
                        )

                title = soup.title.string if soup.title else 'No title found'
                anchors = [a.get_text(strip=True) for a in soup.find_all('a') if a.get_text(strip=True)]
                paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]

                context = {
                    'title': title,
                    'anchors': anchors,
                    'paragraphs': paragraphs,
                    'url': url,
                }

            except Exception as e:
                context['error'] = str(e)
        elif action == 'clear':
            pass
    return render(request, 'scraper/fetch.html', context)
