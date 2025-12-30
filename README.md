# Portafolio

## Proyecto

Plantilla web para programadores desarrollada con la premisa de crear el "portafolio perfecto", con todas las secciones e información fundamental.

<a href="./demo.png"><img src="./demo.png" style="height: 50%; width:50%;"/></a>

* Avatar y datos principales
* Información de contacto, CV y redes
* Sobre mí
* Tecnologías
* Experiencia
* Proyectos
* Formación
* Extra


## Instalación

Puedes seguir la [guía oficial](https://reflex.dev/docs/getting-started/installation/) de Reflex.

Clona el proyecto, crea un entorno virtual, instala Reflex y ejecútalo para acceder al proyecto desde [http://localhost:3000](http://localhost:3000).

`pip install reflex`

`reflex init`

`reflex run`

## Configuración

Principalmente puedes configurar el contenido y el aspecto gráfico del sitio web.

* Contenido: Edita el archivo [data.json](./assets/data/data.json) con la información de tu portafolio.
	* Campos opcionales dentro de `experience`, `projects` y `training`: *technologies, date, certificate, image, url y github*.
	* Los iconos generales se corresponden con los identificadores de [Lucide icons](https://lucide.dev/icons/).
	* Los iconos de las tecnologías se corresponden con los identificadores de [Devicon](https://devicon.dev/).
* Tema: Edita el tema gráfico de la web.
	* Descomenta la línea `rx.theme_panel()` en `portafolio.py`. 
	* Inicia el proyecto, selecciona la configuración que quieras y pulsa `Copy Theme`.
	* Añade esa información dentro de `theme=rx.theme()` en `portafolio.py`.

## Despliegue

![Vercel](https://img.shields.io/github/stars/vercel/vercel?label=Vercel&style=social)

El proyecto utiliza [Vercel](https://vercel.com) como hosting de recursos estáticos.

Se configura el despliegue automático desde los archivos [vercel.json](./vercel.json) y [build.sh](./build.sh).


## ![https://mouredev.com](https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_emote.png) Creditos: Brais Moure.
### Freelance full-stack iOS & Android engineer


Soy ingeniero de software desde 2010. Desde 2018 combino mi trabajo desarrollando Apps con la creación de contenido formativo sobre programación y tecnología en diferentes redes sociales como **[@mouredev](https://moure.dev)**.

