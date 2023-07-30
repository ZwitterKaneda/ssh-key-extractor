import os
import re
import unittest

def extract_ssh_key(file_content):
    private_key_pattern = r"-----BEGIN RSA PRIVATE KEY-----\n(.+?)\n-----END RSA PRIVATE KEY-----"
    certificate_pattern = r"-----BEGIN CERTIFICATE-----\n(.+?)\n-----END CERTIFICATE-----"

    private_key_match = re.search(private_key_pattern, file_content, re.DOTALL)
    certificate_match = re.search(certificate_pattern, file_content, re.DOTALL)

    if private_key_match:
        return private_key_match.group(1), "private"
    elif certificate_match:
        return certificate_match.group(1), "public"
    else:
        return None, None

def save_ssh_key(file_name, key, key_type):
    if key_type == "private":
        file_name = "clave_privadarsa.pem"
        key_header = "RSA PRIVATE KEY"
    elif key_type == "public":
        file_name = "clave_publica.pem"
        key_header = "CERTIFICATE"
    else:
        print("Invalid key type.")
        return

    with open(file_name, 'w') as file:
        file.write(f"-----BEGIN {key_header}-----\n")
        file.write(key)
        file.write(f"\n-----END {key_header}-----")

    print(f"The file \"{file_name}\" has been successfully created.")

def process_files_in_directory(directory):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    target_directory = os.path.join(script_directory, directory)

    for file_name in os.listdir(target_directory):
        if file_name.endswith(".pem"):
            file_path = os.path.join(target_directory, file_name)
            with open(file_path, 'r') as file:
                file_content = file.read()

            key, key_type = extract_ssh_key(file_content)
            if key and key_type:
                save_ssh_key(file_name, key, key_type)
            else:
                print(f"No valid SSH key found in the file {file_name}.")

def main():
    process_files_in_directory("")

if __name__ == "__main__":
    main()

def check_file_contains_lines(file_name, first_line, last_line):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines[0].strip() == first_line and lines[-1].strip() == last_line

class TestScript(unittest.TestCase):
    def test_file_contains_lines(self):
        # Test para el archivo "clave_privadarsa.pem"
        file_name_rsa = "clave_privadarsa.pem"
        self.assertTrue(os.path.isfile(file_name_rsa), f"The file \"{file_name_rsa}\" does not exist.")

        first_line_expected_rsa = "-----BEGIN RSA PRIVATE KEY-----"
        last_line_expected_rsa = "-----END RSA PRIVATE KEY-----"

        self.assertTrue(
            check_file_contains_lines(file_name_rsa, first_line_expected_rsa, last_line_expected_rsa),
            f"The file \"{file_name_rsa}\" does not contain the expected lines."
        )

        # Test para el archivo "clave_publica.pem"
        file_name_cert = "clave_publica.pem"
        self.assertTrue(os.path.isfile(file_name_cert), f"The file \"{file_name_cert}\" does not exist.")

        first_line_expected_cert = "-----BEGIN CERTIFICATE-----"
        last_line_expected_cert = "-----END CERTIFICATE-----"

        self.assertTrue(
            check_file_contains_lines(file_name_cert, first_line_expected_cert, last_line_expected_cert),
            f"The file \"{file_name_cert}\" does not contain the expected lines."
        )
    def tearDown(self):
        # Mensajes finales
        file_name_rsa = "clave_privadarsa.pem"
        file_name_cert = "clave_publica.pem"
        if os.path.isfile(file_name_rsa) and os.path.isfile(file_name_cert):
            print("Ambos archivos fueron creados exitosamente.")
        else:
            print("Uno o más de los archivos no fueron creados correctamente.")

if __name__ == "__main__":
    try:
        unittest.main()
    except:
        pass