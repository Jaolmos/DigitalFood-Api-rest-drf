from rest_framework.routers import DefaultRouter
from payments.api.views import PaymentViewSet

router_payment = DefaultRouter()
router_payment.register(prefix='payments', basename='payments', viewset=PaymentViewSet)