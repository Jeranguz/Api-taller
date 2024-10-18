from rest_framework import serializers
from .models import Juego, Genero, Plataforma

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'

    def create(self, validated_data):
        # Extraer las plataformas antes de usar super()
        plataformas = validated_data.pop('plataformas', [])

        # Si no hay imagen proporcionada, asigna la imagen por defecto
        if 'image' not in validated_data or not validated_data['image']:
            validated_data['image'] = 'game_images/league-of-legends.webp'  # Ruta de la imagen por defecto

        # Llamar al método create original
        juego = super().create(validated_data)

        # Asignar las plataformas usando el método set()
        juego.plataformas.set(plataformas)

        # Retornar la instancia del juego
        return juego