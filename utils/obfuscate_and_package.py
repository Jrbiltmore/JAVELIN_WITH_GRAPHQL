import logging
import subprocess

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compile_to_bytecode(script_path):
    logging.info("Compiling script to bytecode...")
    subprocess.run(['python', '-m', 'compileall', '-b', script_path])
    logging.info("Bytecode compilation completed.")

def obfuscate_code(script_path):
    logging.info("Obfuscating script using PyArmor...")
    subprocess.run(['pyarmor', 'obfuscate', script_path])
    logging.info("Code obfuscation completed.")

def package_executable(script_path):
    logging.info("Packaging script into executable using PyInstaller...")
    subprocess.run(['pyinstaller', '--onefile', '--noconsole', script_path])
    logging.info("Executable packaging completed.")

if __name__ == "__main__":
    script_path = input("Enter the script path to compile, obfuscate, and package: ")
    compile_to_bytecode(script_path)
    obfuscate_code(script_path)
    package_executable(script_path)
    logging.info("All tasks completed successfully.")
