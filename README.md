# OpenCV-SQLite
Proyecto de reconocimiento facial con openCV y conexion a base de datos con sqlite

Estructura de directorios: 

![Estructura](https://user-images.githubusercontent.com/60827293/132273573-2e87ebda-7081-4280-b0f2-600773fcaa14.jpg)


Nota: Dentro de la carpeta recognizer es donde se va a cuardar el archivo con extensión .yml, y mientras en la carpeta dataSet es en donde se van a almacenar las fotografías.

Requisitos:

   - python 3
   - opencv
   - numpy
   - PIL
   - sqlite
   - haarcascade_frontalface_default.xml
   
nota: Este puedes conseguirlo del repositorio oficial de opencv.
-----------------------------------------------------------------------------

Flujo del programa

El flujo del siguiente proyecto es muy sencillo, se trata de un programa que va en primera instancia a capturar el rostro de una persona por medio de diversas fotografias ("datasetCreator.py"), dichas fotografias se estarán almacenando en alguna carpeta que defina el usuario y serviran como la fuente de conocimiento para un programa entrenador que va a encargarse de crear el archivo trainning.yml, este archivo será la fuente de conocimiento para que finalmente nuestro último script denominado detector.py, se encargue solo de evaluar con base a la fuente de conocimientos y a la base de datos el rostro que esta capturando imprimiendo en pantalla la información relacionada a dicho usuario.

-----------------------------------------------------------------------------
Procedimiento

1. Por medio de sqlite, deberás crear una base de datos con el nombre "FaseBase.db", dentro de está base de datos deberás crear una tabla llamada "people" la cual debera contener los siguientes datos:

    - id int primary key 
    - name varchar(80)
    - age varchar(10)

Estos campos son los que se encargará el programa de consultar al final para poder detectar tu rostro.

2. Primero debemos ejecutar el dataSetCreator.py, este script te pedira que ingreses por consola los mismos datos que serán insertados en la base de datos. Sólo cuando hayas ingresado todos los datos, se activará la cámara que comenzará a sacar fotos de tu rostro( procura estar bien iluminado y de frente), estas fotografias estarán nombradas con el id que ingreses, mismo con el cual el programa evaluará al momento de detectar tu rostro contra la base de datos. Recuerda crear una carpeta en donde se van a almacenar todas las fotografias por usuario.

3. Después de tomar las fotografias, deberas ejecutar el trainer.py, este archivo se va a encargar de analizar el rostro captado en todas las fotografias y empezará a generar su fuente de información creandote el archivo recognizer/trainning.yml

4. Finalmente, ejecutamos detector.py, el cual se va a encargar de conectar con la base de datos y a su vez con el archivo recognizer/trainning.yml para hacer una coimparación y empezar a detectar tu rostro. Sí todo ha salido bien, sólo deberas presionar la tecla "q" para que la ventana se cierre y finalice el programa.

CONSEJOS (IMPORTANTE)
Al momento de crear la base de datos, te va a pedir que escojas una ruta donde albacenar el archivo .db. Por lo cual, debes almacenarla dentro de tu carpeta de proyecto como un archivo más.

Ahora, al momento de que estés ejecutando el proyecto puede que te llegue a crear otro archivo con el mismo nombre de la base de datos, es decir otro archivo llamado FaseBase.db, sí ese fuera el caso lo que deberás de hacer es eliminar ese archivo que te creo, el único que puede existir es el que tu guardaste originalmente de la base de datos, de lo contrario no habrá una correcta persistencia de los datos y no funcionará el programa.

 Cuando estes ejecutando el programa, el archivo de la base de datos debe llamarse FaceBase.db, pero una vez que hayas terminado de usarlo, notaras que cuando quieres revisar la base de datos está no estará cargando, no hay que temer pues para solucionarlo solo debes quitar la extension db al archivo principal, es decir que de llamarse FaseBase.db pasará a llamarse FaseBase, de está forma podras consultar con los datos desde tu gestor de sqlite.
