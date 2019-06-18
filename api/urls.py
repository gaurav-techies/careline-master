from django.urls import include, path


urlpatterns = [
    path('users/', include('users.urls')),

    path('leads/', include('leads.urls')),

    path('care/', include('carelineapp.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
]
