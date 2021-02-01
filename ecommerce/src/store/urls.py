from . import views
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
	path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('',views.store,name="store"),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'),
]

