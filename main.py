from fastapi import FastAPI , Path, UploadFile, File
from typing import Optional
from pydantic import BaseModel
import shutil
import uvicorn
import pandas as pd
import numpy as np

app=FastAPI( Title="Consultas de Plataformas", 
description=" Esta API nos permite conocer los diferentes datos de las plataformas Amazon, Netflix, Hulu, Disney",
version="1.0.0.0.1")

df_actores= pd.read_csv('actores.csv')
df_genero= pd.read_csv('generos.csv')
df_unificado=pd.read_csv('general.csv')


@app.get("/max_duration/")
async def get_max_duration(año:int, Plataforma:str, Tipo_Film:str):
    message = f"La maxima duracion segun tipo de film de {Plataforma} es"
    return {message:df_unificado[(df_unificado['Ano_Rodaje']==año)&(df_unificado['Plataforma']==Plataforma)&(df_unificado['medida_tiempo_duracion']== Tipo_Film)]['tiempo_duracion'].max()}


@app.get('/Cantidad de Peliculas y Series/')
async def get_count_plataform(Plataforma:str):
    message = f'La cantidad de peliculas y series en {Plataforma} es '
    return{f"Cantidad de películas en {Plataforma} es":df_unificado[(df_unificado['Plataforma']==Plataforma)&(df_unificado['Tipo_Film']=='Movie')]['Tipo_Film'].count().tolist(),
    f"Cantidad de series en {Plataforma} es":df_unificado[(df_unificado['Plataforma']==Plataforma)&(df_unificado['Tipo_Film']=='TV Show')]['Tipo_Film'].count().tolist()}

@app.get('/Cantidad de veces que se repite genero y plataforma/')
async def get_listedin(genero):
    genero={(df_genero[(df_genero['genero']==genero)]['plataforma'].value_counts().idxmax()):
    (df_genero[(df_genero['genero']==genero)]['plataforma'].value_counts().max().tolist())}
    return genero

@app.get('/Actor que mas se repite/')
async def get_actor(plataforma:str, año:int):
    data = df_actores[(df_actores['año']==año)&(df_actores['plataforma']==plataforma)]['actor']
    # return {data.value_counts().max()}
    if data.value_counts().index[0] == 'sin dato':
        return {data.value_counts().index[1]:data.value_counts()[1].tolist()}
    elif data.value_counts().index[0] != 'sin dato':
        return {data.value_counts().index[0]:data.value_counts()[0].tolist()}
