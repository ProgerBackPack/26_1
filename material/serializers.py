from rest_framework.serializers import ModelSerializer, SerializerMethodField

from material.models import Course, Lesson

class LessonSerializer(ModelSerializer):
    """ Сериализатор Урока """
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """ Сериализатор Курса """
    lesson_count = SerializerMethodField(read_only=True)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson(self, obj):
        return [lesson.name for lesson in obj.lesson_set.count()]

    class Meta:
        model = Course
        fields = '__all__'



class LessonDetailSerializer(ModelSerializer):
    lesson_count = SerializerMethodField(read_only=True)
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Lesson
        fields = ('course', 'title', 'description', 'get_lesson_count')









