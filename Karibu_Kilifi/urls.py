from django.urls import path

from Karibu_Kilifi.views import signup, login_view, SampleHome

urlpatterns = [
        path('signup/', signup, name='signup'),
        path('login/', login_view, name='login'),
        path('home/', SampleHome),

]