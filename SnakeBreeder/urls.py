from django.contrib import admin
from django.urls import path, include

import snake.urls
import lizard.urls

from .views import home, contact
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'', home, name = 'home'),
    path('serpents/', include(snake.urls), name = 'snake'),
    path('lezards/', include(lizard.urls), name = 'lizard'),
    path('services/', include('django.contrib.flatpages.urls'), name = 'services'),
    path('contact/', contact, name = 'contact'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
