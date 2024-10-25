from rest_framework.serializers import ModelSerializer

from material.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """ Сериализатор Курса """
    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(ModelSerializer):
    """ Сериализатор Урока """
    class Meta:
        model = Lesson
        fields = '__all__'


