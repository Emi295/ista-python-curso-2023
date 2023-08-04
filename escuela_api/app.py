import flask
import csv

app = flask.Flask(__name__)


@app.route("/hola_mundo")
def hola_mundo():
    return "<h1>Hola mundo</h1>"
          
@app.route("/mostrar_alumnos")
def lista_alumnos():
    nombre_archivo = "/workspaces/ista-python-curso-2023/datos/estudiante.csv"
    with open(nombre_archivo,'r',encoding='utf-8') as estudiantes:
        lector = csv.reader(estudiantes, delimiter=",")
        #Omite los encabezados
        next(lector,None)
        filas = []
        for fila in lector:
            nombre1 = fila[3]
            nombre2 = fila[4] 
            apellido1= fila[1]
            apellido2= fila[2]
            filas.append(nombre1+" "+nombre2+" "+apellido1+" "+apellido2)
    filas.sort()
    return filas

@app.route("/registrar_asistencia", methods=["POST"])
def agregar_asistencia():
    datos = flask.request.json
    lista = [valor for valor in datos.values()]
    datos_ingresados = "\n" + ",".join(lista)
    with open("/workspaces/ista-python-curso-2023/datos/asistencia.csv", "a") as asistencia:
        asistencia.write(datos_ingresados)
    return "Asistencia registrada con exito"


@app.route("/total_asistencias")
def contar_asistencia():

    parametros = flask.request.args
    
    curso_esperado = parametros['curso']
    cedula_est = parametros['cedula']
    
    if curso_esperado not in ['java','python','ccss']:
        return 'Curso no existe', 400
     
    filas_csv = []

    with open('/workspaces/ista-python-curso-2023/datos/asistencia.csv','r') as asistencia:
        reader = csv.reader(asistencia)
        filas_csv = [fila for fila in reader]

    columnas = filas_csv.pop(0)

    lista_filtrada = []
    for fila in filas_csv:
        if fila[0]==cedula_est and fila[1]==curso_esperado:
            lista_filtrada.append(fila)
        else:
            return f'0 , No hay asistencias para la cedula: {cedula_est} en el curso: {curso_esperado}'

    return f'El total de asistencias es {len(lista_filtrada)}, para la cedula: {cedula_est} en el curso: {curso_esperado}'
