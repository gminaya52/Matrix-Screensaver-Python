# Matrix-Screensaver-Python

Salvapantallas tipo Matrix escrito en Python

El código genera un protector de pantalla al estilo de la película Matrix. ideal para no tener que instalar programas de terceros pesados que pueden no funcionar correctamente.

Se requiere que tengas instalado los módulos pygame, random, os, ctypes, ya que esta versión es ideal si tienes varios monitores, reconoce toda la extensión.

Abre el código, ejecútalo para probarlo. He intentado dejarlo lo más parecido al de Matrix, pero:

Si no estás conforme con la velocidad de caída, puesde modificarlo al final en la sección "clock.tick"

Si no estás conforme con el efecto del destello puedes modificarlo en "fade_surface.set_alpha(50)" 

Si consigues el efecto que quieres, puedes crear el instalable con pyinstaller, siguiendo lo siguiente:

Instala el módulo pyinstaller: ejecuta en un terminal "pip install pyinstaller"

Ejecuta en el terminal (en la misma carpeta dónde tienes el archivo .py) "pyinstaller --onefile --noconsole salvapantallas_Matrix.py"

Si tienes problemas con dónde se instalan tus módulos y que versión de python ejecuta tu terminal, utiliza mejor el comando "py -m PyInstaller --onefile --noconsole salvapantallas_Matrix.py", o llama a la versión de python que tenga el módulo instalado.

Cuando termine de crear el ejecutable, este se creará en la carpeta "dist"

Cambia la extensión del ejecutable de "exe" a "scr"

Instala el salvapantallas. Sino tienes la opción de instalarlo directamente, copia el archivo.scr a la ruta "C:\Windows\System32"

Ahora solo ve a la configuración de salvapantallas de windows y selecciona Matrix, o el nombre que le hayas puesto.
