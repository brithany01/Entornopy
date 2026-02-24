💄 Generador de Productos de Maquillaje
📌 Documentación del Proyecto
🧩 1. Planteamiento del problema

Se desarrolló un programa en Python que permite al usuario consultar diferentes categorías de maquillaje y visualizar información organizada sobre cada una.

El objetivo fue crear una aplicación sencilla en consola que demostrara el uso de estructuras de datos, funciones y librerías externas.

🛠 2. Tecnologías Utilizadas

Lenguaje: Python 3.12.0

Librería externa: rich

Entorno virtual: venv

Control de versiones: Git

Repositorio remoto: GitHub

🧠 3. Lógica de Programación Implementada

El sistema fue desarrollado utilizando:

🔹 Diccionarios

Se creó un diccionario principal llamado categorias_maquillaje, el cual contiene:

Nombre de la categoría

Descripción

Lista de productos asociados

Ejemplo de estructura utilizada:

categorias_maquillaje = {
    "correctores": {
        "descripcion": "...",
        "productos": [...]
    }
}

Esto permitió organizar la información de forma estructurada y accesible.

🔹 Funciones

Se implementó una función llamada mostrar_categoria() que:

Recibe como parámetro el nombre de la categoría.

Verifica si la categoría existe en el diccionario.

Muestra la información correspondiente.

En caso de no existir, muestra un mensaje de error.

Esto permite reutilizar código y mantener una estructura limpia.

🔹 Entrada de Datos

Se utilizó la función input() para permitir que el usuario escribiera la categoría deseada desde la consola.

categoria_usuario = input("Escribe una categoría: ")
🔹 Uso de Librería Externa (Rich)

Se integró la librería rich para:

Mostrar paneles visuales en consola.

Aplicar colores y formato.

Mejorar la experiencia visual del usuario.

Se importaron:

from rich.console import Console
from rich.panel import Panel

Y se utilizó Console() para imprimir contenido estilizado.

🗂 4. Estructura del Proyecto

El proyecto fue organizado de manera profesional incluyendo:

Archivo principal .py

Archivo requirements.txt

Entorno virtual

Archivo README.md

Esto permite que cualquier persona pueda clonar el repositorio y ejecutar el proyecto sin problemas.

🔄 5. Control de Versiones

Se utilizó Git para:

Registrar cambios mediante commits.

Subir el proyecto a GitHub.

Mantener una versión organizada del código.

Comandos utilizados:

git add .

git commit -m "mensaje"

git push

🎯 6. Resultados

El programa cumple con:

Mostrar categorías correctamente.

Validar entrada del usuario.

Presentar información estructurada.

Mantener código limpio y organizado.

Incluir documentación y dependencias necesarias.

📈 7. Aprendizajes Obtenidos

Durante el desarrollo del proyecto se reforzaron conocimientos sobre:

Diccionarios en Python

Funciones

Validaciones

Entornos virtuales

Instalación de librerías externas

Git y GitHub

Documentación técnica en Markdown