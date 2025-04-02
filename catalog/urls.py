from django.urls import path
from catalog.views import (
    index,
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookListView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
    about_us_view,
    contacts_view,
)


urlpatterns = [
    path("", index, name="index"),
    path("dish/", DishListView.as_view(), name="dish"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path(
        "dish_type/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_type/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("cook/", CookListView.as_view(), name="cook"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cook/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("about_us/", about_us_view, name="about_us"),
    path("contacts/", contacts_view, name="contacts"),
]

app_name = "catalog"
