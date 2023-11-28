import os
import re
import shutil


def es_snake_case(nombre):
    return re.match(r'^[a-z0-9]+(_[a-z0-9]+)*$', nombre)


# Nombre del proyecto
print("Creation of a flask app ")
while True:
    name_project = input("project name: ")

    if es_snake_case(name_project):
        break
    else:
        print("the name is not valid")

# carpetas de origen y destino para copiar los archivo
dirOrigen = os.path.join(os.path.dirname(__file__), "src")
dirProject = os.path.join(os.getcwd(), name_project)

# lista de archivos y carpetas ignorados
listIgnore = shutil.ignore_patterns('.vscode', '.venv', '__pycache__')

# Copia todos los archivos de origen a destino
try:
    shutil.copytree(dirOrigen, dirProject, symlinks=False,
                    ignore=listIgnore)
except Exception as ex:
    print("Error", ex)
