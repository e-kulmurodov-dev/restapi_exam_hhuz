# from django.db.models import Count
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import OrderingFilter
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.throttling import UserRateThrottle
# from rest_framework.viewsets import ModelViewSet
#
# from apps.filters import ProductFilter
# from apps.models import Category, Product, Employer
# from apps.serializers import CategoryModelSerializer, ProductModelSerializer, UserModelSerializer, \
#     VacancyModelSerializer

# Create your views here.
#
# class CategoryListCreateAPIView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer
#     # permission_classes = IsAuthenticated, AllowAny
#     throttle_classes = [UserRateThrottle]
#
#     def get_queryset(self):
#         return Category.objects.annotate(product_count=Count('product')).filter(product_count__gt=0)
#
#
# class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryModelSerializer
#
#     # http_method_names = ['delete'] restriction
#
#
# class ProductListCreateAPIView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer


# class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductModelSerializer


# class ProductModelViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductListModelSerializer
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     filterset_class = ProductFilter
#     ordering_fields = ['price', 'created_at']
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ProductListModelSerializer
#         return ProductDetailModelSerializer


# -------------------------------------------------------------------------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.filters import VacancyFilter
from apps.models import User, Vacancy
from apps.serializers import UserModelSerializer, VacancyModelSerializer, OTPRequestSerializer, \
    OTPVerifySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

from root import settings


class EmployerListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class EmployerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class VacancyListCreateAPIView(ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilter


class VacancyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyModelSerializer


class OTPRequestView(APIView):
    permission_classes = AllowAny,

    def post(self, request, *args, **kwargs):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.save()
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp.otp}',
                settings.EMAIL_HOST_USER,
                [otp.user.email],
                fail_silently=False,
            )
            return Response({"message": "OTP sent to email"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OTPVerifyView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "OTP verified", "user_id": user.id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
