from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("edit",views.edit,name="edit"),
    path("editdata/<int:id>",views.editdata,name="editdata"),
    path("deletedata/<int:id>",views.deletedata,name="deletedata"),
]
