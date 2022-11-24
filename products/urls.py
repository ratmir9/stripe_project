from django.urls import path
from products.views import (
    SuccessTemplateView,
    CancelTemplateView,
    ItemDetailView,
    BuyProduct
)


urlpatterns = [
    path('success/', SuccessTemplateView.as_view(), name='success'),
    path('cancel/',CancelTemplateView.as_view(), name='cancel'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='detail-item'),
    path('buy/<int:id>/', BuyProduct.as_view(), name='buy-product')
]
