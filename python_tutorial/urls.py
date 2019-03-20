"""python_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from sandbox.views import LoginView, MainSiteView, logout_view, RegisterView, AddBuiltInFunctionView,  \
    HomeView, LessonView, ExamView, AddExamView, AdminToolsView, AddStringMethodsView, \
    AddListMethodsView, AddDictionaryMethodsView, AddTupleMethodsView, AddSetMethodsView, AddKeywordsView,  \
    LibraryView, SearchView, DeleteDataView, DeleteRedirectView, UserView, UserMessagesView, UserWriteMessageView


urlpatterns = [
    #  ---------------admin site--------------------------------
    path('admin/', admin.site.urls),
    url(r'admin/add_built_in_function/', AddBuiltInFunctionView.as_view()),
    url(r'admin/add_string_methods/', AddStringMethodsView.as_view()),
    url(r'admin/add_list_methods/', AddListMethodsView.as_view()),
    url(r'admin/add_dictionary-methods/', AddDictionaryMethodsView.as_view()),
    url(r'admin/add_tuple-methods/', AddTupleMethodsView.as_view()),
    url(r'admin/add_set-methods/', AddSetMethodsView.as_view()),
    url(r'admin/add_keywords/', AddKeywordsView.as_view()),
    url(r'admin/add_exam/', AddExamView.as_view()),
    url(r'^admin_tools/$', AdminToolsView.as_view()),
    url(r'^admin/delete_data/$', DeleteDataView.as_view()),
    url(r'^admin/delete_data/redirect/$', DeleteRedirectView.as_view()),

    #  ----------------main site--------------------------------
    url(r'^start/$', LoginView.as_view()),
    url(r'^main/$', MainSiteView.as_view(), name='main'),
    url(r'^logout/$', logout_view),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^home/$', HomeView.as_view()),
    url(r'^exam/$', ExamView.as_view()),
    url(r'^library/(?P<element>(\w)+)', LibraryView.as_view()),
    url(r'^search/$', SearchView.as_view()),
    url(r'^user/$', UserView.as_view()),
    url(r'^user/messages/$', UserMessagesView.as_view()),
    url(r'^user/write_message/$', UserWriteMessageView.as_view()),

    #  --------------------vertical nav--------------------------
    url(r'^lesson/(?P<lesson_number>(\d)+)$', LessonView.as_view()),
]
