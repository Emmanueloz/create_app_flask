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

# Creación de las carpetas del proyecto
os.mkdir(name_project)
os.mkdir(f"{name_project}/app")
os.mkdir(f"{name_project}/app/static")
os.mkdir(f"{name_project}/app/templates")
os.mkdir(f"{name_project}/app/routes")
os.mkdir(f"{name_project}/app/api")

# carpetas de origen y destino para copiar los archivo
dirOrigen = os.path.join(os.path.dirname(__file__), "app")
dirProject = os.path.join(os.getcwd(), name_project)
dirModuleProject = os.path.join(dirProject, "app")
ls_app = os.listdir(dirOrigen)


for elemento in ls_app:
    try:
        if elemento == "__init__.py":
            print(f"Copiando {elemento} --> {dirModuleProject} ... ", end="")
            src = os.path.join(dirOrigen, elemento)  # origen
            # destino en la carpeta module
            dst = os.path.join(dirModuleProject, elemento)
            shutil.copy(src, dst)
            print("Correcto")
            continue
        print(f"Copiando {elemento} --> {dirProject} ... ", end="")
        src = os.path.join(dirOrigen, elemento)  # origen
        dst = os.path.join(dirProject, elemento)  # destino
        shutil.copy(src, dst)
        print("Correcto")
    except:
        print("Falló")
        print("Error, no se pudo copiar el archivo. Verifique los permisos de escritura")
