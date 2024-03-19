from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Todo model.

    This serializer is used to convert Todo model instances to JSON and vice versa.
    It defines the fields that should be serialized and deserialized.

    Attributes:
        text: A CharField representing the text of the todo item.

    Methods:
        create(validated_data): Creates a new todo item instance in the database.
        update(instance, validated_data): Updates an existing todo item instance in the database.
    """

    text = serializers.CharField(max_length=1000, required=True)

    def create(self, validated_data):
        """
        Creates a new todo item instance in the database.

        Args:
            validated_data: A dictionary containing the validated data from the request.

        Returns:
            The newly created todo item instance.
        """
        return Todo.objects.create(
            text=validated_data.get('text')
        )

    def update(self, instance, validated_data):
        """
        Updates an existing todo item instance in the database.

        Args:
            instance: The todo item instance to be updated.
            validated_data: A dictionary containing the validated data from the request.

        Returns:
            The updated todo item instance.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    class Meta:
        model = Todo
        fields = (
            'id',
            'text'
        )
