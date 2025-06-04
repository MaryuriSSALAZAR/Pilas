# Pilas
Planteamiento del Ejemplo: Procesamiento de Tareas en un Servidor Web
Imagina un servidor web que necesita manejar muchas solicitudes de usuarios al mismo tiempo. Para evitar que el servidor se sature, a menudo se utiliza una cola de tareas. Sin embargo, en ciertos escenarios donde la última solicitud recibida debe ser procesada primero (quizás porque es la más reciente o más crítica), una pila puede ser una estructura de datos útil.

Elementos Clave:

Solicitudes (o Tareas): Cada solicitud que llega al servidor (por ejemplo, cargar una imagen, actualizar un perfil de usuario, enviar un mensaje) se considera una tarea.
Recepción de Solicitudes: A medida que las solicitudes llegan, se añaden a la pila.
Procesamiento de Solicitudes: El servidor siempre toma y procesa la solicitud que está en la cima de la pila.
