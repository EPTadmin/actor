from rest_framework import serializers
from . models import *


    
    
class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('__all__')
    


class PositionActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Position_Activity
        fields = ('type','emne', 'antall_time','arsverk')



class PersonSerializers(serializers.ModelSerializer):
    
    class Meta:


        model = Person
        fields = ('id','first_name','last_name','courses','position','groupe','activities')

    def to_representation(self, instance):
        self.fields['courses'] = CourseSerializers(many=True,read_only=True)
        return super(PersonSerializers,self).to_representation(instance)



class PersonCourseSerializers(serializers.ModelSerializer):

    person_full = serializers.SerializerMethodField()
    course_full = serializers.SerializerMethodField()

    class Meta:
        model = PersonCourse
        fields = ['id','person','course','person_full','course_full','amount']

    def get_person_full(self,obj):
        return obj.person.first_name + ' ' + obj.person.last_name 
    
    def get_course_full(self,obj):
        return obj.course.course_id + ' ' + obj.course.name 

class PersonActivitySerializers(serializers.ModelSerializer): 
    person_full = serializers.SerializerMethodField()
    activity_full = serializers.SerializerMethodField() 

    class Meta:
        model = PersonActivity
        fields = ['id','person','person_full','activity','activity_full', 'amount']

    def get_person_full(self,obj):
        return obj.person.first_name + ' ' + obj.person.last_name 
    
    def get_activity_full(self,obj):
        return obj.activity.type 

