from rest_framework import  serializers
from . import models



class DynamicSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):


        fields = kwargs['context'].pop('fields', None)
        exclude = kwargs['context'].pop('exclude', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)
        if fields is not None:
            # Only include the specified fields
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude is not None:
            # Exclude the specified fields
            for field_name in exclude:
                self.fields.pop(field_name, None)



