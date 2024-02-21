from rest_framework import serializers
from .models import Student
import re

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ['name', 'age']
        fields = '__all__'    # to serialize all fields
        # exclude = ['id']      # to remove a perticuler field

    def validate(self, data):   # model data validation

        if data['age'] < 18:
            raise serializers.ValidationError({'error':'age cannot be less than 18'})
        
        if data.get('name'):
            name_data = data['name']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')
            if not regex.search(name_data) == None:
                raise serializers.ValidationError({'error':'name cannot be numeric'})
            
            return data
                
            