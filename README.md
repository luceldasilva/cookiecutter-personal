# Plantilla de Cookiecutter

Esta es una plantilla de cookiecutter para Data Science desarrollado en [Curso de Configuración Profesional de Entorno de Trabajo para Ciencia de Datos](https://platzi.com/cursos/entorno-ciencia-datos/) en ![platzi](https://platzi.com)


## Requerimientos

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

Puedes usar pip:

``` bash
pip install cookiecutter
```

o en todo caso conda:

``` bash
conda install -c conda-forge cookiecutter
```

## Crear nuevo proyecto

Puedes crear en tu entorno base u otro entorno que instalaste cookiecutter

```bash
cookiecutter https://github.com/luceldasilva/cookiecutter-personal
```

Luego vas a la carpeta {{ cookiecutter.project_slug }}:
- Instalar el entorno de trabajo con su archivo environment.yml
- Leer los archivos README.md e install.md

## Créditos

Al profe de Platzi [Jesús Vélez Santiago](https://platzi.com/profes/jvelezmagic/) [con su github jvelezmagic](https://github.com/jvelezmagic/cookiecutter-conda-data-science) 

Su proyecto está fuertemente influenciado por [drivendata's Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science), [andfanilo's Cookiecutter for Kaggle Conda projects](https://github.com/andfanilo/cookiecutter-kaggle), y el paquete de Julia [DrWatson](https://juliadynamics.github.io/DrWatson.jl/dev/).

Otros enlaces que ayudaron a dar forma a este cookiecutter:

- [Write less terrible code with Jupyter Notebook](https://blog.godatadriven.com/write-less-terrible-notebook-code)
- [Cookiecutter DataScience Opinions](http://drivendata.github.io/cookiecutter-data-science/#opinions)