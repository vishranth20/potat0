from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
            path('',views.index,name='index'),
            path('pay',views.pay),
            path('scam',views.scam),
            path('admin/', admin.site.urls),
            path('profile',views.profile,name='profile'),
            path('logout',views.logoutUser,name='logout'),
            path('hotels/<str:destination>',views.hotels,name='hotels'),
            path('login',views.loginPage,name='login'),
            path('hotels/<str:destination>/<str:hotel>',views.dish,name='hotels'),
            path("register", views.register, name="register")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

posts = [
        {
                'Name': 'Vishranth',
                'Post': 'CEO',
                'School': 'Saraswathi vidyalaya',
                'Company': 'of POTATO food app'
        },
        {
                'Name': 'Pranesh',
                'Post': 'Chairman',
                'School': 'Saraswathi vidyalaya',
                'Company': 'of POTATO food app'
        },

        {
                'Name': 'Deepak',
                'Post': 'Manager',
                'School': 'Saraswathi vidyalaya',
                'Company': 'of POTATO food app'
        }
]