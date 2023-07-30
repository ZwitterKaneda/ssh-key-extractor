# SSH Key Extractor

![Python](https://img.shields.io/badge/python-3.x-blue.svg)

El "SSH Key Extractor" es una herramienta escrita en Python que te permite extraer claves SSH (tanto públicas como privadas) de archivos PEM en el formato adecuado para su uso.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio en tu máquina local:

```
git clone https://github.com/tu-usuario/ssh-key-extractor.git
```
2. Ve al directorio del proyecto:
```
cd ssh-key-extractor
```
3. Ejecuta el script principal para procesar los archivos PEM y extraer las claves SSH:

```
python ssh-key-extractor.py

```

## Uso

- Coloca tus archivos PEM en el directorio del proyecto.
- Ejecuta el script principal `ssh-key-extractor.py`.
- El script procesará todos los archivos PEM en el directorio y creará los archivos de clave correspondientes.

## Archivos creados

- Las claves privadas se guardarán en el archivo "clave_privadarsa.pem".
- Las claves públicas se guardarán en el archivo "clave_publica.pem".

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu función o mejora:
```
git checkout -b mi-nueva-funcion
```

3. Realiza tus cambios y commit:
```
git commit -m "Agrega mi nueva función"
```

4. Envía tus cambios al repositorio en GitHub:
```
git push origin mi-nueva-funcion
```

5. Crea una solicitud de pull en GitHub.
6. Espera a que tus cambios sean revisados y fusionados con el repositorio principal.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

## Contacto

Si tienes preguntas o comentarios sobre este proyecto, por favor contáctame a través de mi correo electrónico: smentek@gmail.com.
