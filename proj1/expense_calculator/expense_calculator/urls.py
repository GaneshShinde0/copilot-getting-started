"""expense_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import include, path

# create a router for expenses
from expenses import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'expenses', views.ExpenseViewSet)

urlpatterns = [
	# add api url
	# Configure rest_framework browsable api
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]


admin.site.site_header = 'Expense Calculator Admin'