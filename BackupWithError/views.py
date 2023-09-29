from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import BackupWithError
from .serializer import BackupWithErrorSerializer
import requests

class BackupWithErrorListView(generics.ListCreateAPIView):
    queryset = BackupWithError.objects.all()
    serializer_class = BackupWithErrorSerializer

    def list(self, request):
        try:
            # Configuración de la solicitud a la API de Acronis
            base_url = "https://us-cloud.acronis.com/api"
            url = f"/valut_manager/v1/backups"
            headers = {
                "Authorization": "Bearer ",
                "Content-Type": "application/json"  
            }

            # Realizar la solicitud GET
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            # Crear o actualizar registros en el modelo BackupWithError
            for item in data:
                backup_id = item.get("backup_id")
                error_message = item.get("error_message")

                # Usar get_or_create para evitar consultas innecesarias a la base de datos
                obj, created = BackupWithError.objects.get_or_create(
                    backup_id=backup_id,
                    defaults={"error_message": error_message}
                )

            # Serializar y devolver los datos
            queryset = BackupWithError.objects.all()
            serializer = BackupWithErrorSerializer(queryset, many=True)
            return Response(serializer.data)

        except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (p. ej., conexión fallida)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            # Manejar otros errores, como respuestas no válidas
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)