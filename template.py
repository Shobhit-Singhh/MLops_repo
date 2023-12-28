import os

def create_directories():
    directories = ['data', 'documents', 'logs', 'models', 'pipelines', 'src', 'test', 'utils']

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, '__init__.py'), 'w') as init_file:
            pass

def create_files():
    files = ['config.yaml', 'main.py', 'README.md', 'requirements.txt']

    for file in files:
        with open(file, 'w') as new_file:
            pass

if __name__ == "__main__":
    create_directories()
    create_files()
