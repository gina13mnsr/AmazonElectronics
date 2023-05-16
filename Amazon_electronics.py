import requests
import csv
from io import StringIO

# URL del archivo CSV en el sitio web
url = "https://data.world/datafiniti/amazon-and-best-buy-electronics/file/DatafinitiElectronicsProductData.csv"

# Realizar la solicitud HTTP al servidor y obtener la respuesta
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Obtener el contenido del archivo CSV como texto
    csv_text = response.text

    # Crear un objeto StringIO para leer el texto como archivo CSV
    csv_file = StringIO(csv_text)

    # Leer el archivo CSV con la biblioteca csv
    reader = csv.reader(csv_file)

    # Iterar sobre las filas del archivo CSV
    for row in reader:
        # Procesar cada fila como desees
        print(row)
else:
    print("Error al acceder al archivo CSV. Código de respuesta:", response.status_code)
