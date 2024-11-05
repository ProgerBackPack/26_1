from rest_framework import serializers

from material.models import Course, Lesson, Subscription
from material.validators import YoutubeValidation

class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор Урока """
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [YoutubeValidation(field="url_video")]


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор Курса """
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson(self, obj):
        return [lesson.name for lesson in obj.lesson_set.count()]

    class Meta:
        model = Course
        fields = '__all__'


class LessonDetailSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Lesson
        fields = ('course', 'title', 'description', 'get_lesson_count')

class SubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор Подписки """

    class Meta:
        model = Subscription
        fields = "__all__"