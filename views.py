from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import DetailView,ListView
from .models import Lint
from .forms import FormNew
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def NewView(request):
	x = request.GET.get('form210')
	if x !=None and  int(x)>0 and int(x)<100:
		for i in range (int(x)):
			q = Lint(title='Номер {}'.format(i),cifra='{}'.format(i))
			q.save()
		return HttpResponseRedirect('/something/detail/')
	return render(request,('something/new.html'))
	
def NewNew(request):
	queryset_list = Lint.objects.all()
	paginator = Paginator(queryset_list, 1) 
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
        
		queryset = paginator.page(1)
	except EmptyPage:
        
		queryset = paginator.page(paginator.num_pages)
	context = {
			'object_list':queryset,
			'title':Lint.cifra,
			
	}
	return render(request,('something/detail.html'),context)
	
	
