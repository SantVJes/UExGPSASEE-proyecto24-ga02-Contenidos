# API Contenidos

## Descripción
El **Microservicio de Contenidos** es una solución diseñada para gestionar eficientemente los contenidos dentro de una plataforma, proporcionando un punto centralizado y escalable para manejar todos los datos relacionados con los contenidos. Su propósito principal es garantizar una integración fluida con otros microservicios del sistema y el frontend de la aplicación, asegurando una experiencia de usuario personalizada y dinámica.

### Funcionalidades Principales

- **Gestión de Contenidos**:
  - **Creación de Contenidos**: Permite agregar nuevos contenidos a la plataforma, validando los datos necesarios para mantener la integridad de la información.
  - **Consulta de Contenidos**: Facilita la búsqueda y recuperación de contenidos, ya sea de manera individual o listando todos los contenidos disponibles.
  - **Actualización de Contenidos**: Proporciona la capacidad de modificar detalles de contenidos existentes, como título, descripción, imágenes, etc.
  - **Eliminación de Contenidos**: Permite eliminar contenidos de manera segura, garantizando que los datos sean gestionados correctamente.

- **Integración con Microservicios**:
  - **Microservicio de Usuarios**: Se comunica con la API de usuarios para obtener y gestionar las preferencias de los usuarios, como sus contenidos favoritos y datos relacionados con su interacción con la plataforma.
  - **Microservicio de Vistas**: Este microservicio recibe información sobre los contenidos más vistos y las interacciones de los usuarios, lo que permite generar estadísticas y recomendaciones personalizadas basadas en los comportamientos de visualización.
  - **Microservicio de Recomendaciones**: A partir de los datos proporcionados por el microservicio de contenidos y vistas, ofrece recomendaciones personalizadas a los usuarios, mejorando su experiencia dentro de la plataforma.

- **Interacción con el Frontend**:
  - El microservicio expone una API REST que permite al frontend realizar operaciones de consulta, actualización y eliminación de contenidos.
  - Soporte para operaciones de consulta y visualización en tiempo real, lo que facilita la actualización dinámica de contenidos en el frontend.

### Beneficios Clave

- **Eficiencia y Escalabilidad**: Está diseñado para manejar grandes volúmenes de contenido sin comprometer el rendimiento de la plataforma.
- **Integración Fluida**: Actúa como un puente entre los microservicios de usuarios y vistas, asegurando la consistencia y sincronización de los datos de contenido a través de todos los componentes del sistema.
- **Experiencia Personalizada**: Gracias a la integración con el servicio de vistas y las recomendaciones personalizadas, la plataforma puede ofrecer contenido relevante para cada usuario en tiempo real.
- **Modularidad**: Al estar basado en una arquitectura de microservicios, este componente es fácilmente mantenible y escalable, lo que facilita la implementación de nuevas funcionalidades en el futuro.

### Casos de Uso

1. **Creación de Nuevo Contenido**:
   Un administrador o un sistema automatizado crea un nuevo contenido en la plataforma. El microservicio valida los datos y lo almacena en la base de datos, después de lo cual la información es disponible para su visualización o recomendación.

2. **Actualización de Contenido**:
   Un contenido existente necesita ser actualizado (por ejemplo, cambiar la descripción o agregar nuevas etiquetas). El microservicio procesa y almacena la actualización, asegurándose de que el contenido modificado sea accesible de inmediato para los usuarios.

3. **Eliminación de Contenido**:
   Cuando un contenido es eliminado, el microservicio asegura que se eliminen todos los datos asociados a este y que no sea mostrado en ninguna parte de la plataforma, manteniendo la consistencia de la información.

4. **Recomendaciones Personalizadas**:
   Usando el comportamiento de los usuarios y sus preferencias, la API de contenidos trabaja junto con el microservicio de recomendaciones para sugerir contenido relevante basado en los intereses del usuario. Estas recomendaciones son dinámicas y se ajustan a medida que los usuarios interactúan con la plataforma.

---
## 📃 Más Información sobre el Método de Desarrollo sobre La Refactorizacion

[Infome de la Cuarta Entrega sonar cloud](https://github.com/UExGPSASEE/proyecto24-ga02/wiki/📡-Entrega-Trabajo-4:-SonarCloud)

## Requisitos  
Python 3.5.2 o superior  

## Uso  
Para ejecutar el servidor, por favor sigue los siguientes pasos desde el directorio raíz:  

```
pip3 install --no-cache-dir -r requeriments_sqlalchemy.txt
pip3 install -r requirements.txt
python3 -m openapi_server
```

Luego, abre tu navegador y dirígete a la siguiente URL:

```
http://localhost:8080/ui/
```
