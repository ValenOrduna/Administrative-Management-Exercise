# Administrative Management Civitec

Administrative Management es un proyecto diseñado para la administración de un sistema de multas de la policía de manera sencilla y segura. Este sistema permite acceder a los datos de manera fácil y rápida, mientras mantiene la seguridad necesaria para el uso de los mismos. El objetivo de este proyecto es facilitar la visualización, actualización o inserción de datos, brindando una herramienta eficiente y efectiva para la gestión de multas.

## Requisitos

- Tener instalado Python 3 en el equipo.
- # Tener dependencia Django instalada

# Administrative Management Civitec

Administrative Management es un proyecto diseñado para la administración de un sistema de multas de la policía de manera sencilla y segura. Este sistema permite acceder a los datos de manera fácil y rápida, mientras mantiene la seguridad necesaria para el uso de los mismos. El objetivo de este proyecto es facilitar la visualización, actualización o inserción de datos, brindando una herramienta eficiente y efectiva para la gestión de multas.

## Requisitos

- Tener instalado Python 3 en el equipo.
- Tener dependencia Django instalada

## Instalación

Pasos a seguir para la instalacion del proyecto:

- Clonar el repositorio del proyecto en tu máquina local usando git:
- `git clone https://github.com/ValenOrduna/Administrative-Management-Exercise.git `
- Ejecutar el siguiente comando para descargar las dependencias necesarias:
- `pip install -r requirements.txt`
- Crear superusuario:
- `cd administrative-managment`
- `python manage.py createsuperuser`
- Puedes utilizar los usuarios creados:
- ADMIN: valentin_orduña CLERK: agustin_orduña OFFICER: matias_orduña OFFICER: magali_zibana
- Todos tienen la siguiente contraseña para facilitar la entrada y salida en modo de prueba: admin4853

## Tecnologías

El proyecto se realizo con el Framework Django. Uno de los principales beneficios de Django es su arquitectura de modelos, que me permitió crear y administrar fácilmente los modelos de base de datos necesarios para la aplicación. También utilicé muchas de las aplicaciones integradas de Django, como el panel de administración y el sistema de autenticación de usuarios, lo que me permitió crear una aplicación robusta y segura.

En cuanto al diseño y estilos, utilicé Tailwind. Elegí Tailwind por su facilidad de uso y su capacidad para personalizar los estilos con facilidad. Me gustó especialmente la forma en que Tailwind utiliza clases predefinidas para estilizar los componentes, lo que me permitió trabajar con el HTML y CSS de una manera más sencilla y organizada.

## Detalles Técnicos

Para el login de los usuarios se requiere que un administrador cree sus cuentas. Esta es una medida de seguridad que permite controlar el acceso a la aplicación. Para iniciar sesión, los usuarios deben proporcionar su nombre de usuario y contraseña. Tuve dos opciones para el nombre de usuario: la primera era utilizar el número de placa, ya que es único. Sin embargo, esto puede ser confuso y frustrante para los policías que tienen que ingresar constantemente. La segunda opción que elegí fue utilizar el nombre y apellido, separados por un guión bajo (\_). Esta opción es más intuitiva para los oficiales, pero puede presentar problemas a largo plazo si dos oficiales tienen el mismo nombre y apellido.

En cuanto a la gestión de datos, es fundamental brindar opciones accesibles y seguras a los usuarios para poder interactuar con los mismos. En este sentido, opté por utilizar dos formas de acceso a los datos: el Django Admin y los endpoints validados.

El Django Admin es una herramienta potente y completa que ofrece una interfaz gráfica de usuario para la administración de los datos. Permite visualizar y editar los datos de manera rápida y sencilla, brindando una experiencia amigable para aquellos usuarios que prefieren trabajar con interfaces visuales.

Por otro lado, los endpoints validados permiten la interacción con los datos a través de una API REST. Esta opción brinda una mayor flexibilidad en cuanto a la gestión de datos, permitiendo la automatización de procesos y la integración con otras herramientas y sistemas.

La combinación de estas dos opciones proporciona una experiencia más completa y versátil en cuanto a la gestión de datos. Los usuarios pueden elegir la opción que más se ajuste a sus necesidades y preferencias, permitiendo un acceso más sencillo y seguro a los datos del sistema

## Mejoras Futuras

Existen varias mejoras que se pueden implementar en el proyecto para hacerlo más eficiente y completo. Una de las principales mejoras que se puede hacer es la mejora del diseño de la aplicación. Esto incluye la mejora de la interfaz de usuario para que sea más fácil de usar y atractiva para el usuario final. Además, se puede optimizar el rendimiento de la aplicación para que se cargue más rápido y se ejecute de manera más eficiente.

Además, se pueden insertar nuevos endpoints en la aplicación para agregar más funcionalidad. Por ejemplo, se puede agregar un endpoint que permita a los oficiales de policía ver un resumen de todas las multas que han emitido en un período de tiempo determinado. También se pueden agregar endpoints para permitir a los usuarios de la aplicación descargar informes detallados de las multas emitidas en un período de tiempo determinado.

## Videos Demostrativos

[Video Demostracion](https://vimeo.com/814829852)

## Contacto

[Linkedin](https://www.linkedin.com/in/valentinorduna/)

[GitHub](https://github.com/ValenOrduna)
