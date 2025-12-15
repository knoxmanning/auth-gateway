# Library import
import os

# Define project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define project name
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

# Define author information
AUTHOR_NAME = "Your Name"
AUTHOR_EMAIL = "your@email.com"

# Define license information
LICENSE_NAME = "MIT License"
LICENSE_URL = "https://opensource.org/licenses/MIT"

# Print project information
print(f"Project: {PROJECT_NAME}")
print(f"Author: {AUTHOR_NAME} <{AUTHOR_EMAIL}>")
print(f"License: {LICENSE_NAME} ({LICENSE_URL})")