#bikeshare_data urls
from django.conf.urls import url
from bikeshare_data import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
	url(r'^about/$', views.AboutPageView.as_view()), #adds about page url
	url(r'^data/$', views.DataPageView.as_view()),
	url(r'^index/$', views.HomePageView.as_view()),
	url(r'^avgdist/$', views.AvgDistPageView.as_view()),
	url(r'^commute/$', views.CommutePageView.as_view()),
	url(r'^seasonal/$', views.SeasonalPageView.as_view())
]