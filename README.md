Práctica de Laboratorio 1: Control de Versiones con Git (Fundamentos)
Propósito:
Poner en prácitca lo aprendido sobre el uso de comandos básicos de Git Bash
para contorlar la terminal y organizar los archivos que necesitemos en nuestro directorio.

Instrucciones:
Para ejecutar el programa auth_service.py que acabamos de crear, solo necesitas tener Python instalado en tu computadora. Sigue estos pasos según tu sistema operativo:

1. Requisitos previosVerifica que tienes Python instalado abriendo tu terminal (consola) y ejecutando:Bashpython --version
(Si no funciona, prueba con python3 --version)

2. Pasos para la ejecuciónGuarda el código:
Copia el código anterior y guárdalo en un archivo de texto plano llamado exactamente auth_service.py.Abre la terminal / consola:
Dirígete a la carpeta o directorio donde guardaste el archivo usando el comando cd:Bashcd ruta/a/la/carpeta
Ejecuta el script:
Escribe el siguiente comando y presiona Enter:Bashpython auth_service.py
(O si usas Mac/Linux o tu entorno requiere la versión específica: python3 auth_service.py)

3. Resultado esperado en pantallaAl ejecutarlo, la terminal te mostrará el resultado de las pruebas integradas en el bloque principal:Plaintext--- Probando auth_service.py ---
Login admin (correcto): True
Login admin (incorrecto): False
Login usuario inexistente: False
