from django.shortcuts import render
from paste.models import Paste
from django.template import RequestContext
from django.shortcuts import redirect
import string
import random

def main(request):
	posted = request.POST.get('paste', -1)
	title = request.POST.get('title', -1)
	if (posted != -1) and (title != -1):
		randString = random_generator()
		while Paste.objects.filter(url=randString).count() > 0:
			randString = random_generator()
		
		p = Paste(title=title,url=randString,content=posted)
		p.save()
		return redirect('/'+ randString)
	else:
		return render(request, 'paste/index.html')
	
def fetch_paste(request):
	urlget = request.META.get('PATH_INFO', '')[1:]
	p = Paste.objects.get(url=urlget)
	return render(request, 'paste/paste.html', {'paste':p})
# Create your views here.
def random_generator():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
