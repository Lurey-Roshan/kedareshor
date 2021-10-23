from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404
# Create your views here.
from blog.models import Notice
from blog.forms import NoticeForm,EditNoticeForm


def home(request):
	return render(request, 'blog/home.html')





def notice_index(request):
	notice=Notice.objects.all()
	context={
		'notice':notice
	}
	return render( request,'blog/notice.html', context)

	

def notice_detail(request, id):
	notice=get_object_or_404(Notice, pk=id)
	context={
			'notice':notice
	}
	return render(request,'blog/notice_detail.html', context)

def create_notice(request):
	if request.user.is_staff:
		form=NoticeForm()
		if request.method=="POST":
			form=NoticeForm(request.POST, request.FILES)

			if form.is_valid():
				form.save()
				return HttpResponse("NOtices Created Successfully")

		context={
			'form':form
		}
		return render(request, 'blog/create-notice.html', context)


	else:
		return HttpResponse("You are not registered User, Contact admin")


def edit_notice(request, id):
	if request.user.is_staff:
		notice=get_object_or_404(Notice, pk=id)
		form=EditNoticeForm(instance = notice)
		if request.method=="POST":
			form=EditNoticeForm(request.POST, request.FILES, instance=notice)

			if form.is_valid():
				form.save()
				return HttpResponse("NOtices Updated Successfully")

		context={
			'form':form
		}
		return render(request, 'blog/create-notice.html', context)


	else:
		return HttpResponse("You are not registered User, Contact admin")



def delete_notice(request, id):
	if request.user.is_staff:
		notice=get_object_or_404(Notice, pk=id)
		notice.delete()
		return HttpResponse("NOtices Deleted Successfully")
	else:
		return HttpResponse("You are not authorized User, Contact admin")