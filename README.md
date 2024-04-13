# Portafolio "perfecto" para programadores

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.5+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)

[![HTML](https://img.shields.io/badge/HTML-orange?style=for-the-badge&logo=html5&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-blue?style=for-the-badge&logo=css3&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow?style=for-the-badge&logo=javascript&logoColor=white&labelColor=101010)](https://developer.mozilla.org/es/docs/Web/JavaScript)

## Publicar en GitHub Pages

### Crear un environment 

Estas son las instrucciones para crear un environment llamado `github-pages`:

1. Navega a las Settings de tu repositorio.
2. Abre `Environments` en la sección `Code and automation`.
3. Presiona el botón `New environment`.
4. En el nombre ingresa `github-pages`.
5. En la sección `Deployment branches and tags`, click en el menú que dice `No restricion`.
6. Del menú desplegable, seleccionar `Selected branches and tags`.
7. Un nuevo panel debió haber aparecido, click en `Add deployment branch or tag rule`.
8. Escribe el nombre de tu rama principal, generalmente `main`.
9. Haz click en `Add rule`.

Debe quedar algo así:

<a href="./environment_setup.png"><img src="./environment_setup.png" style="height: 50%; width:50%;"/></a>

### Publicar

Para publicar nuevas versiones de tu portafolio, debes hacerlo con la acción `🚀 Publicar GitHub Pages`.

1. Navega a `Actions`.
2. Selecciona `🚀 Publicar GitHub Pages`
3. Click en `Run workflow`
4. Ten en cuenta que solo funciona desde la rama `main`.
5. Click en `Run workflow`.

## Actualizar datos personales

### Datos de la página

Abrir el archivo `./assets/data/data.json`.

Inspeccionarlo y colocar los datos según creas correcto.

Alternativamente, puedes usar como base el archivo de plantilla `data_template.json`.

IMPORTANTE: el archivo que quieras usar se debe llamar `data.json`. Si decides usar la plantilla base, recuerda renombrarla.

## Plantilla de portafolio web minimalista configurable a nivel gráfico y de contenido.

Desarrollado utilizando [Python](https://python.org) y [Reflex](https://reflex.dev), disponible para desplegar de forma estática (HTML, CSS, JS).

#### Proyecto realizado durante emisiones en directo desde [Twitch](https://twitch.tv/mouredev)
> ##### Si consideras útil el proyecto, apóyalo haciendo "★ Star" en el repositorio. ¡Gracias!

## Portafolio

<a href="https://youtu.be/zFbTXe1yFGA"><img src="http://i3.ytimg.com/vi/zFbTXe1yFGA/maxresdefault.jpg" style="height: 50%; width:50%;"/></a>

¿Qué información debo añadir en mi portafolio como desarrollador? En [este](https://youtu.be/zFbTXe1yFGA) vídeo explico el por qué de cada apartado.

Tras el análisis, elaboré un esquema para reflejar la información obligatoria, recomendable, opcional y desaconsejada de la web.

![Esquema portafolio](https://mouredev.com/images/portafolio.jpg)

Con esta premisa he desarrollado este proyecto web que refleja de manera real toda la información de nuestro "portafolio perfecto".

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

**Demo: [https://portafolio-template.vercel.app/](https://portafolio-template.vercel.app/)**

<a href="./live_demo.png"><img src="./live_demo.png" style="height: 50%; width:50%;"/></a>

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

Aquí tienes la [demo](https://portafolio-template.vercel.app/).

## Curso de Python desde cero
### Aprende Python desde sus fundamentos

<a href="https://github.com/mouredev/hello-python"><img src="https://raw.githubusercontent.com/mouredev/Hello-Python/main/Images/header.jpg"/></a>

Si quieres aprender desde cero, tienes gratis todos los tutoriales que he creado. Más de 37 horas desde fundamentos, frontend, backend o integración con IA.

[![Curso Python](https://img.shields.io/github/stars/mouredev/hello-python?label=Curso%20Python%20desde%20cero&style=social)](https://github.com/mouredev/hello-python)

Si quieres unirte a nuestra comunidad de desarrollo, aprender programación de Apps, mejorar tus habilidades y ayudar a la continuidad del proyecto, puedes encontrarnos en:

[![Twitch](https://img.shields.io/badge/Twitch-Programación_en_directo-9146FF?style=for-the-badge&logo=twitch&logoColor=white&labelColor=101010)](https://twitch.tv/mouredev)
[![Discord](https://img.shields.io/badge/Discord-Servidor_de_la_comunidad-5865F2?style=for-the-badge&logo=discord&logoColor=white&labelColor=101010)](https://mouredev.com/discord)
[![Link](https://img.shields.io/badge/Links_de_interés-moure.dev-39E09B?style=for-the-badge&logo=Linktree&logoColor=white&labelColor=101010)](https://moure.dev)

## ![https://mouredev.com](https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_emote.png) Hola, mi nombre es Brais Moure.
### Freelance full-stack iOS & Android engineer

[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCxPD7bsocoAMq8Dj18kmGyQ?style=social)](https://youtube.com/mouredevapps?sub_confirmation=1)
[![Twitch Status](https://img.shields.io/twitch/status/mouredev?style=social)](https://twitch.com/mouredev)
[![Discord](https://img.shields.io/discord/729672926432985098?style=social&label=Discord&logo=discord)](https://mouredev.com/discord)
[![Twitter Follow](https://img.shields.io/twitter/follow/mouredev?style=social)](https://twitter.com/mouredev)
![GitHub Followers](https://img.shields.io/github/followers/mouredev?style=social)
![GitHub Followers](https://img.shields.io/github/stars/mouredev?style=social)

Soy ingeniero de software desde 2010. Desde 2018 combino mi trabajo desarrollando Apps con la creación de contenido formativo sobre programación y tecnología en diferentes redes sociales como **[@mouredev](https://moure.dev)**.

### En mi perfil de GitHub tienes más información

[![Web](https://img.shields.io/badge/GitHub-MoureDev-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/mouredev)
