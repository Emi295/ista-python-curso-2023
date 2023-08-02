import flask
import csv

app = flask.Flask(__name__)

@app.route("/lista_alumnos")
def mostrar_listaAlumnos():
    
    nombre_archivo = "/workspaces/ista-python-curso-2023/datos/estudiante.csv"
    with open(nombre_archivo, "r") as estudiantes:
        lector = csv.reader(estudiantes, delimiter=",")
        # Omitir el encabezado
        next(lector, None)
        for fila in lector:
            # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
            nombre1 = fila[3]
            nombre2 = fila[4]
            apellido1= fila[1]
            apellido2= fila[2]
      return( f"'{nombre1}{nombre2}{apellido1}{apellido2}")