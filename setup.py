from cx_Freeze import setup, Executable
import os

# List of Python scripts to be included as executables
executables = [
    Executable('main.py')
]

# Additional files or directories to be included (if any)
additional_files = [
    # ('relative_path_from_project', 'destination_path_in_build_directory')
    ('vosk-model-en-in-0.5', 'vosk-model-en-in-0.5'),
    ('vosk-model-hi-0.22', 'vosk-model-hi-0.22'),
]

# Function to collect all subdirectories
def collect_subdirectories(folder):
    subdirs = []
    for root, dirs, files in os.walk(folder):
        for dir in dirs:
            subdirs.append((os.path.join(root, dir), os.path.join(root, dir)))
    return subdirs

# Collect all subdirectories under 'vosk-model-en-in-0.5' and 'vosk-model-hi-0.22'
additional_folders = collect_subdirectories('vosk-model-en-in-0.5') + collect_subdirectories('vosk-model-hi-0.22')

# Add additional subdirectories
additional_files.extend(additional_folders)

# Configuration for cx_Freeze
setup(
    name='YourProjectName',
    version='1.0',
    description='Description of your project',
    executables=executables,
    options={
        'build_exe': {
            'includes': [],  # List additional modules to include
            'include_files': additional_files,  # Include additional files and folders
            # Optionally exclude modules that aren't needed
            # 'excludes': ['tkinter'],
        }
    }
)

