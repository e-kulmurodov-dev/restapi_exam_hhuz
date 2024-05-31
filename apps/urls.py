from django.urls import path

from apps.views import EmployerRetrieveUpdateDestroyAPIView, EmployerListCreateAPIView, VacancyListCreateAPIView, \
    VacancyRetrieveUpdateDestroyAPIView, OTPRequestView, OTPVerifyView

urlpatterns = [
    path('employer', EmployerListCreateAPIView.as_view()),
    path('employer/<int:pk>', EmployerRetrieveUpdateDestroyAPIView.as_view()),
    path('vacancy', VacancyListCreateAPIView.as_view()),
    path('vacancy/<int:pk>', VacancyRetrieveUpdateDestroyAPIView.as_view()),

    path('otp/request/', OTPRequestView.as_view(), name='otp-request'),
    path('otp/verify/', OTPVerifyView.as_view(), name='otp-verify'),
]
