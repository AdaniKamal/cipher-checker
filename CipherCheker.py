import requests
import sys
from colorama import Fore, Style, init #color

# Initialize colorama
init()

def check_cipher_security(cipher_name):
    url = f"https://ciphersuite.info/api/cs/{cipher_name}/" #API fetch info
    response = requests.get(url)
    
    if response.status_code == 200:
        cipher_data = response.json()
        if cipher_name in cipher_data:
            security_status = cipher_data[cipher_name].get('security', 'unknown')
            return security_status
        else:
            return "Cipher suite information not found"
    else:
        return "Error fetching data"

#color status
def display_security_status(cipher_name, security_status):
    color_map = {
        'weak': Fore.YELLOW,
        'insecure': Fore.RED,
        'recommended': Fore.BLUE,
        'secure': Fore.GREEN
    }
    
    color = color_map.get(security_status.lower(), Fore.WHITE)
    print(f"{cipher_name} --> {color}{security_status.capitalize()}{Style.RESET_ALL}")

def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                cipher_name = line.strip()
                if cipher_name:
                    security_status = check_cipher_security(cipher_name)
                    display_security_status(cipher_name, security_status)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

#To analyse based on input. Single cipher or Multiple cipher (<cipher>.txt)
def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python this_file_name.py single <single cipher_name>")
        print("  python this_file_name.py file <file>.txt")
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    
    if mode == 'single':
        if len(sys.argv) != 3:
            print("Usage: python this_file_name.py single <single cipher_name>")
            sys.exit(1)
        cipher_name = sys.argv[2]
        security_status = check_cipher_security(cipher_name)
        display_security_status(cipher_name, security_status)
    
    elif mode == 'file':
        if len(sys.argv) != 3:
            print("Usage: python this_file_name.py file <file>.txt")
            sys.exit(1)
        file_path = sys.argv[2]
        process_file(file_path)
    
    else:
        print("Invalid mode. Use 'single' for one cipher or 'file' for a file of ciphers.")

if __name__ == "__main__":
    main()

#Cipher Cheker by AdaniKamal
