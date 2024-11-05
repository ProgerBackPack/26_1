from django.urls import path

from rest_framework.routers import SimpleRouter

from material.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDeleteAPIView, SubscriptionCreateAPIView
from material.apps import CoursesConfig

app_name = CoursesConfig.name

router = SimpleRouter()
router.register("course", CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/create', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
    path('subscription/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
]

urlpatterns += router.urls