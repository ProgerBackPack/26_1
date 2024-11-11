from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import Users, Payments
from users.serializers import UserSerializer, PaymentsSerializer




class UserList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()
    permission_classes =(AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()



class UserDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Users.objects.all()


class PaymentsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['date_payment']



