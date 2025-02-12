# ========== HELPER FUNCTIONS MODULE========== #

import os
from configuration import DESTINATION_FOLDERS, SOURCE_FOLDER

def initialize_folders():
    """Create destination folders."""
    for folder in DESTINATION_FOLDERS.values():
        folder_path = os.path.join(SOURCE_FOLDER, folder)
        os.makedirs(folder_path, exist_ok=True)
    print("Folders created!")