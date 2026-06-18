import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mysql_credentials = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),   # default is 'localhost'
    'user': os.getenv('MYSQL_USER', 'car_user'),
    'password': os.getenv('MYSQL_PASSWORD', 'CarPass123!'),
    'database': os.getenv('MYSQL_DATABASE', 'car_damage_detection'),
}

# Optional: Add unix_socket if specified in .env
if os.getenv('MYSQL_SOCKET'):
    mysql_credentials['unix_socket'] = os.path.expanduser(os.getenv('MYSQL_SOCKET'))
