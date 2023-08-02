import flask
import csv

app = flask.Flask(__name__)

nombre_archivo = "datos/estudiante.csv" /workspaces/ista-python-curso-2023/datos/estudiante.csv
with open(nombre_archivo, "r") as estudiantes:
    lector = csv.reader(estudiantes, delimiter=",")
    # Omitir el encabezado
    next(lector, None)
    for fila in lector:
        # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
        nombre = fila[0]
        calificacion = int(fila[1])
        precio = float(fila[2])
        print(
            f"Juego: '{nombre}' con calificación {calificacion} y precio {precio}")