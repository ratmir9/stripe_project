from django.views.generic import (
    View, 
    DetailView,
    TemplateView
)
from django.conf import settings
from django.http import Http404, JsonResponse

from products.models import Item
from products.services import create_checkout_session, get_product_by_id


class SuccessTemplateView(TemplateView):
    template_name = 'success.html'


class CancelTemplateView(TemplateView):
    template_name = 'cancel.html'


class ItemDetailView(DetailView):
    model = Item 
    template_name = 'item-detail.html'
    pk_url_kwarg = 'id'
    
    def get_object(self, queryset=None):
        item = get_product_by_id(self.kwargs['id'])
        if not item:
            raise Http404(f'Item with id = {self.kwargs["id"]} not')
        return item
        
    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context.update({
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context


class BuyProduct(View):
    def get(self, request, id, *args, **kwargs):
        item = get_product_by_id(id=id)
        if not item:
            raise Http404(f'Item with id = {id} not')
        domain = 'http://' + request.get_host()
        checkout_session = create_checkout_session(item, domain)
        return JsonResponse({
            'id': checkout_session.id
        })
