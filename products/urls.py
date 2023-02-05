from .views import product_list, category_list

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('categories/', category_list, name='category-list'),
]