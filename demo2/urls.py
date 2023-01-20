
from django.contrib import admin
from django.urls import path, include
from product import views
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    #path('', article_views.article_list, name='home'),
    path('', article_views.ArticleListView.as_view(), name='home'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
