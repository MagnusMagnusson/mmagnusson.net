from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from cv import views as cvViews
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import redirect


def redirect_to_default_language(request):
    return redirect(f'/{settings.LANGUAGE_CODE}/')

urlpatterns = [
        path('', redirect_to_default_language)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main_site.routes')),
)
