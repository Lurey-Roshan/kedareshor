from django.urls import path,include

from blog import	views



urlpatterns=[
		path('',views.home, name='home'),
		path('create-notice', views.create_notice, name='create_notice'),
		path('edit-notice/<id>/edit',views.edit_notice, name='edit_notice'),
		path('notice/<id>/delete', views.delete_notice, name='delete_notice'),
		path('notice', views.notice_index, name='notice_index'),
		path('notice/<id>/detail',views.notice_detail, name='notice_detail')
	]