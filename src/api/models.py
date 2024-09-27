from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_lanzamiento = models.DateField()
    compania = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataformas = models.ManyToManyField(Plataforma, related_name='juegos')
    image = models.ImageField(upload_to='game_images/')

    def save(self, *args, **kwargs):
        # Si hay una imagen, la convertimos a .webp antes de guardar
        if self.image:
            # Abrir la imagen usando PIL
            img = Image.open(self.image)
            
            # Convertir la imagen a webp en memoria
            webp_image = BytesIO()
            img.save(webp_image, format='WEBP', quality=85)  # Ajustar calidad si es necesario
            
            # Crear un nuevo archivo en memoria con la imagen .webp
            webp_image.seek(0)  # Regresar al inicio del archivo BytesIO
            
            # Asignar el nuevo nombre con la extensión .webp basado en el nombre del juego
            new_filename = f"{self.nombre}.webp"
            self.image = ContentFile(webp_image.getvalue(), new_filename)

        # Guardar la imagen convertida con el nuevo nombre
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
