from django.conf.urls import url

from views import get_test, create_user

urlpatterns = [
    url(r'^test', get_test, name="get_test"),
    url(r'^users/create', create_user, name="create_user")
]
