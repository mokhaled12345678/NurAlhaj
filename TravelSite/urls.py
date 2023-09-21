"""TravelSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from UserView import views, utils
from django.conf import settings
from django.conf.urls.static import static
from payments import views as payviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_packages/', utils.get_packages, name='get_packages'),
    path('booking/<str:location>', views.booking, name='booking'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name="register"),
    path('', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('payments/<str:location>/<str:hotel>', payviews.HomePageView, name='homePay'),
    path('config/', payviews.stripe_config),
    path('create-checkout-session/<str:location>/<str:hotel>/', payviews.create_checkout_session, name='checkout'),
    path('success/', payviews.SuccessView.as_view()), # new
    path('cancelled/', payviews.CancelledView.as_view()), # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)