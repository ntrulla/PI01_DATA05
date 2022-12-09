<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

¡Bienvenidos a mi primer proyecto individual! 
En esta ocasión, les voy a mostrar el paso a paso del proceso de ETL que realice en donde se ingestaron los datos desde diversas fuentes que fueron provistas de diferentes extensiones, como *csv* o *json*. Luego aplique las transformaciones que considere pertinentes, para poder tener disponibles los datos limpios ya que van a ser usados en su consulta a través de una API construida en un entorno virtual dockerizado.

<hr>  

## **Proceso de ETL**

1) Se ingestan los datos provistos en la carpeta Datasets, en el repositorio.<sup>*</sup>
2) Se realiza la limpieza de datos para cada dataset y se corrigen los tipos de datos, valores nulos y duplicados, entre otras tareas.
3) Se relacionan los datasets para poder acceder a su información por medio de consultas a la API.

## **Creacion de la API**

1) Se implementa el codigo de la FASTAPI mediante un archivo main.py, en el cual se van a importar las librerias a usar: 
-from fastapi import FastAPI , Path, UploadFile, File
-from typing import Optional
-from pydantic import BaseModel
-import shutil
-import uvicorn
-import pandas as pd
-import numpy as np
2) Se declara la aplicacion app=FastAPI()
3) Se define el metodo raiz para que me redireccione, este es de tipo GET. Con este metodo le indicamos la ruta en la que queremos que escuche nuestra peticion.

## **Entonro Docker**




