from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('add/',views.add,name="add"),
    path('done/<int:id>',views.done,name="done"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('cancel/<int:id>',views.cancel,name="cancel")
]