
from django import forms 

from blog.models import Notice




class NoticeForm(forms.ModelForm):
	class Meta:
		model = Notice
		fields = "__all__"


class EditNoticeForm(forms.ModelForm):
	class Meta:

		model = Notice
		fields = "__all__"