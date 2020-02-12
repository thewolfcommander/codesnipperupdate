from django.urls import path, include
from .views import snippet_list, snippet_detail

urlpatterns = [
    path('snippets/', snippet_list, name='snippet_list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),
    path('api/', include('api.urls')),
]
