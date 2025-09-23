#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
# esta línea no se debe borrar, importante al momento de crear el ejecutable
# Actualizado al 27 Agosto 2019

from tkinter import *
from tkinter import messagebox


import getpass
import pathlib
import os
import random
import sys

#import playsound

# Función para crear el archivo OCAD.sty con todas las configuraciones necesarias
def create_ocad_sty(folder_path):
    ocad_content = '''% OCAD.sty - Paquete básico para documentos CEPRE-UNI
\\NeedsTeXFormat{LaTeX2e}
\\ProvidesPackage{OCAD}[2025/09/23 Basic OCAD package]

\\RequirePackage{graphicx}
\\RequirePackage{enumerate}
\\RequirePackage[spanish]{babel}
\\RequirePackage{amsmath}
\\RequirePackage{amssymb}
\\RequirePackage{amsfonts}
\\RequirePackage{geometry}

% Comando para incluir figuras con escala
\\newcommand{\\pg}[2]{\\includegraphics[scale=#1]{#2}}

% Comando para crear opciones de respuesta (choices to display)
\\newcommand{\\ctd}[5]{
\\begin{enumerate}[A)]
\\item #1
\\item #2  
\\item #3
\\item #4
\\item #5
\\end{enumerate}
}

% Comando para opciones de verdadero/falso
\\newcommand{\\ctdt}[5]{
\\begin{enumerate}[A)]
\\item #1
\\item #2  
\\item #3
\\item #4
\\item #5
\\end{enumerate}
}

% Comandos de abreviación comunes
\\newcommand{\\al}{\\alpha}
\\newcommand{\\bt}{\\beta}
\\newcommand{\\gm}{\\gamma}
\\newcommand{\\dl}{\\delta}
\\newcommand{\\ep}{\\epsilon}
\\newcommand{\\te}{\\theta}
\\newcommand{\\lm}{\\lambda}
\\newcommand{\\sg}{\\sigma}
\\newcommand{\\om}{\\omega}

% Comando para fracciones
\\newcommand{\\df}[2]{$\\dfrac{#1}{#2}$}

% Comando para llaves grandes
\\newcommand{\\lr}[1]{\\left\\{#1\\right\\}}

% Comandos matemáticos adicionales
\\newcommand{\\ds}{\\displaystyle}
\\newcommand{\\cv}{\\cap}

% Comandos trigonométricos
\\newcommand{\\se}{\\sin}
\\newcommand{\\co}{\\cos}
\\newcommand{\\ta}{\\tan}
\\newcommand{\\rc}[1]{\\sqrt{#1}}
\\newcommand{\\enp}[1]{\\left(#1\\right)}
\\newcommand{\\enl}[1]{\\left\\{#1\\right\\}}
\\newcommand{\\ig}[2]{\\includegraphics[#1]{#2}}

% Comandos adicionales para símbolos matemáticos
\\newcommand{\\Z}{\\mathbb{Z}}
\\newcommand{\\N}{\\mathbb{N}}
\\newcommand{\\R}{\\mathbb{R}}
\\newcommand{\\Q}{\\mathbb{Q}}

\\endinput'''
    
    with open(os.path.join(folder_path, 'OCAD.sty'), 'w', encoding='utf-8') as f:
        f.write(ocad_content)


#### definicion de funciones #####
# funcion que comparador de listas, p1 y p2 son las listas a compara
def iguales(p1,p2):
    for i in range(len(p1)):
        if p1[i]==p2[i]: 
            return True
    return False

# genera las listas de preguntas para 4 temas, 'n' es el número de preguntas
def ruleta(n):
	p1=[]
	for i in range(n):
		p1.append(i)		
	p2=random.sample(p1,len(p1))
	p3=random.sample(p1,len(p1))
	p4=random.sample(p1,len(p1))
	while iguales(p1,p2) == True:
		p2=random.sample(p1,len(p1))
	while (iguales(p3,p1) or iguales(p3,p2)) == True:
		p3=random.sample(p1,len(p1))
	while (iguales(p4,p1) or iguales(p4,p2) or iguales(p4,p3)) == True:
		p4=random.sample(p1,len(p1))
	return [p1,p2,p3,p4]

	
# busca en la cadena la clave 
def letra(c):
	# c es una variable tipo cadena
	c=c.lower()
	if 'a' in c: return 'A'
	if 'b' in c: return 'B'
	if 'c' in c: return 'C'
	if 'd' in c: return 'D'
	if 'e' in c: return 'E'

# lee las carpetas que hay
asignaturas = os.listdir()
#print(asignaturas)
#print(len(asignaturas))
#print(asignaturas[0])

asig=[]

#print(os.path.isdir(asignaturas[0]))

for i in range(len(asignaturas)):
	if os.path.isdir(asignaturas[i]) == True:
		#print(asignaturas[i])
		asig.append(asignaturas[i])
	

#print(asig)
#print(asig[asig.index('fisica')])

temas = ['P','Q','R','S']

num_temas = 4



def exam():
	if len(periodo.get()) != 0:
		fecha = periodo.get()
		# crea las carpetas con los archivos del los examenes
		for i in range(num_temas):
			os.system('mkdir Prueba%s' % temas[i])
			
			# Crear el archivo OCAD.sty en cada carpeta
			create_ocad_sty('Prueba%s' % temas[i])
			
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'\documentclass[12pt,twocolumn]{article}'+'\n'+r'\usepackage{OCAD}'+'\n'+r'\usepackage{import}'+'\n'+r'\usepackage{fancyhdr}'+
					'\n'+r'\usepackage[margin=2cm, top=3cm, bottom=2.5cm]{geometry}'+'\n'+'\n'+r'\setlength\columnsep{1cm}'+'\n'+'\n'+r'\newcommand{\tema}{%s }' % temas[i]+'\n'+'\n')
			prueba.write(r'\fancyhead[CO,CE]{ADMISIÓN %s \hfill CEPRE - UNI  \\ \vspace{0.2cm}  \textbf{1er EXAMEN PARCIAL - CICLO PREUNIVERSITARIO}' % fecha +
						 '\n'+r'\vspace{0.2cm} \hrule\vspace{0.05cm}  \hrule\hrule\hrule\vspace{-0.6cm} }'+
						 '\n'+r'\renewcommand{\headrulewidth}{0pt}'+'\n'+r'\fancyfoot[C]{{\Large \textbf{\tema - \thepage}}}'+
						 '\n'+r'\setlength{\headheight}{40pt}'+'\n'+r'\setlength{\headsep}{0.8cm}'+'\n'+r'\setlength{\footskip}{1cm}'+'\n'+'\n')            
			prueba.write(r'\newcommand{\rpt}[1]{Rpt: #1}'+'\n'+r'%% Anular la siguiente línea para obtener las claves '+
						'\n'+r'\renewcommand{\rpt}[1]{}'+'\n'+'\n'
						+r'\newcounter{nx}'+'\n'+r'\pagestyle{fancy}'+'\n'+'\n'+
						r'\begin{document}'+'\n'+'\n')

		### fisica
		preguntas = os.listdir(asig[asig.index('fisica')])
		# genera lista con 4 listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'\begin{center}'+'\n'+r'\textbf{%s}' % 'FÍSICA' +'\n'+r'\end{center}'+'\n'+r'\begin{enumerate}[1.]'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../%s/%s/}{%s}' % ('fisica',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('%s/%s/visor.tex' % ('fisica',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n')

		### Quimica
		preguntas = os.listdir(asig[asig.index('quimica')])
		# genera lista con 4 listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'\begin{center}'+'\n'+r'\textbf{%s}' % 'QUÍMICA' +'\n'+r'\end{center}'+'\n'+r'\begin{enumerate}[1.]'+'\n'+
						r'\setcounter{enumi}{\value{nx}}'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../%s/%s/}{%s}' % ('quimica',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('%s/%s/visor.tex' % ('quimica',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n')
			
		### Matematica
		# lista las carpetas dentro de matematica
		matematica = os.listdir('matematica')

		### Artimetica
		preguntas = os.listdir( 'matematica/%s' % matematica[matematica.index('aritmetica')])
		# genera lista con 4 listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'\begin{center}'+'\n'+r'\textbf{%s}' % 'MATEMÁTICA'  +'\n'+r'\end{center}'+'\n')
			prueba.write(r'%%% Aritmetica '+'\n')
			prueba.write(r'\begin{enumerate}[1.]'+'\n'+ r'\setcounter{enumi}{\value{nx}}'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../matematica/%s/%s/}{%s}' % ('aritmetica',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('matematica/%s/%s/visor.tex' % ('aritmetica',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n')
			
		#### Algebra
		preguntas = os.listdir( 'matematica/%s' % matematica[matematica.index('algebra')])
		# genera lista con 4 listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'%%% Algebra '+'\n')
			prueba.write(r'\begin{enumerate}[1.]'+'\n'+ r'\setcounter{enumi}{\value{nx}}'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../matematica/%s/%s/}{%s}' % ('algebra',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('matematica/%s/%s/visor.tex' % ('algebra',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n')

		#### Geometria
		preguntas = os.listdir( 'matematica/%s' % matematica[matematica.index('geometria')])
		# genera lista con 4 listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'%%% Geometria '+'\n')
			prueba.write(r'\begin{enumerate}[1.]'+'\n'+ r'\setcounter{enumi}{\value{nx}}'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../matematica/%s/%s/}{%s}' % ('geometria',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('matematica/%s/%s/visor.tex' % ('geometria',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n')			

		#### Trigonometria
		preguntas = os.listdir( 'matematica/%s' % matematica[matematica.index('trigonometria')])
		# genera lista con 4 listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'%%% Trigonometria '+'\n')
			prueba.write(r'\begin{enumerate}[1.]'+'\n'+ r'\setcounter{enumi}{\value{nx}}'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../matematica/%s/%s/}{%s}' % ('trigonometria',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('matematica/%s/%s/visor.tex' % ('trigonometria',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n')			

		### Aptitud academica
		preguntas = os.listdir(asig[asig.index('aptitud_academica')])
		# genera lista con 4 listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'\begin{center}'+'\n'+r'\textbf{%s}' % 'RAZONAMIENTO MATEMÁTICO' +'\n'+r'\end{center}'+'\n'+r'\begin{enumerate}[1.]'+'\n'+
						r'\setcounter{enumi}{\value{nx}}'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../%s/%s/}{%s}' % ('aptitud_academica',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('%s/%s/visor.tex' % ('aptitud_academica',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n') 
						
		### Humanidades
		preguntas = os.listdir(asig[asig.index('humanidades')])
		# genera lista con  listas de numeros aleatorios
		preg = ruleta(len(preguntas))
		for i in range(num_temas):
			# abre el tema
			prueba=open('Prueba%s/Prueba%s.tex' % (temas[i],temas[i]),mode='a',encoding='utf-8')
			prueba.write(r'\begin{center}'+'\n'+r'\textbf{%s}' % 'HUMANIDADES' +'\n'+r'\end{center}'+'\n'+r'\begin{enumerate}[1.]'+'\n'+
						r'\setcounter{enumi}{\value{nx}}'+'\n')
			for j in range(len(preg[i])):
				prueba.write(r'\item \import{../%s/%s/}{%s}' % ('humanidades',preguntas[preg[i][j]],preguntas[preg[i][j]] )+'\n')
				clave=open('%s/%s/visor.tex' % ('humanidades',preguntas[preg[i][j]]),mode='r',encoding='utf-8')
				rpt=clave.readlines()
				prueba.write(r'\rpt{%s} ' % letra(rpt[9][12:20]) +'\n' )
				clave.close
			prueba.write(r'\setcounter{nx}{\value{enumi}}'+'\n'+r'\end{enumerate}'+'\n'+r'\end{document}') 	
	
	else:
		messagebox.showinfo('Error','Escribir el ciclo')


#print('Exámenes creados')
#playsound.playsound('creados.mp3', True)

win = Tk()
win.title("OFICINA CENTRAL DE ADMISIÓN")
win.geometry("620x300+600+400")
win.resizable(0,0)

titulo = Label(win,text="1er Examen Parcial\nCEPRE-UNI",font=("serif",20),padx=20,pady=20)
titulo.pack()

fr1 = Frame(win)
fr1.pack()

lab1 = Label(fr1,text="Escribir el ciclo:",font=("serif",18),padx=20,pady=20)
lab1.grid(row=0,column=0)

periodo = StringVar()
entrada = Entry(fr1, textvariable = periodo,bd=10,relief=SUNKEN,font=("serif",18))
entrada.focus()
entrada.grid(row=0,column=1)

lab4 = Label(fr1,text=" ",width=3)
lab4.grid(row=0,column=2)

fr2 = Frame(win)
fr2.pack()

btg = Button(fr2,text="Generar\nExámenes",font=("serif",18),padx=5,pady=5,command=exam,bg="yellow",borderwidth=10)
btg.grid(row=0,column=0)

lab2 = Label(fr2,text=" ",width=30)
lab2.grid(row=0,column=1)

bts = Button(fr2,text="SALIR",font=("serif",18),padx=5,pady=5,bg="yellow",borderwidth=10,command= lambda:sys.exit())
bts.grid(row=0,column=2)

lab3 = Label(fr2,text= " ",height=1)
lab3.grid(row=1,column=1)



win.mainloop()
