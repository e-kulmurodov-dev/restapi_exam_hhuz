# from rest_framework.fields import SerializerMethodField
# from rest_framework.serializers import ModelSerializer
# from apps.models import Category, Product, ProductImage
#
#
# class ProductImageModelSerializer(ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = 'id', 'image'
#
#
# class ProductListModelSerializer(ModelSerializer):
#     # v_count = SerializerMethodField(method_name='get_vowel_count')
#     images = ProductImageModelSerializer(source='productimage_set', many=True, read_only=True)
#
#     class Meta:
#         model = Product
#         exclude = 'description',
#     #
#     # def vowel_count(self, obj: Product):
#     #     return sum(True for i in obj.description if i not in 'auioe')
#
#     # def to_representation(self, instance: Product):
#     #     represent = super().to_representation(instance)
#     #     represent['category'] = CategoryModelSerializer(
#     #         instance.category,
#     #         context={'request': self.context['request']}).data
#     #     return represent
#
#
# # class ProductDetailModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = Product
# #
# #     def to_representation(self, instance: Product):
# #         represent = super().to_representation(instance)
# #         represent['category'] = CategoryModelSerializer(instance.category).data
# #         return represent
# #
# #
# # class ProductModelSerializer(ModelSerializer):
# #     class Meta:
# #         model = Product
# #         fields = '__all__'
#
# class CategoryModelSerializer(ModelSerializer):
#     product = ProductListModelSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Category
#         fields = '__all__'


# from .models import Product, Category, ProductImage, Employer
#

# class ProductModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'price', 'description']
#
#
# class CategoryModelSerializer(serializers.ModelSerializer):
#     products = ProductModelSerializer(source='product_set', many=True, read_only=True)
#
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'image', 'products']
#         #
#         # def get_products(self, obj):
#         #     products = obj.product_set.all()  # Access the related products
#         #     return ProductModelSerializer(products, many=True).data
#
#
# class ProductImageModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ['id', 'image', 'product']
#

# --------------------------------------------------------------------------------

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.models import OTP
from apps.models import Vacancy, User


class VacancyModelSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = 'password',


class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def create(self, validated_data):
        OTP.objects.filter(user=self.user).delete()
        otp = OTP.objects.create(user=self.user)
        return otp


class OTPVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            self.user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        try:
            otp = OTP.objects.get(user=self.user, otp=data['otp'])
        except OTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP.")

        if otp.expires_at < timezone.now():
            raise serializers.ValidationError("OTP has expired.")

        return data

    def create(self, validated_data):
        otp = OTP.objects.get(user=self.user, otp=validated_data['otp'])
        otp.delete()
        return self.user
