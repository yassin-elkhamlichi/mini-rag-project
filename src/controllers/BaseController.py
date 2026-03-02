from helpers.config import getSetting
from pathlib import Path
import random
import string

class BaseController:

   def  __init__(self):
      self.app_settings = getSetting()
      """
      Initialize the Project Root Directory.

      This line dynamically determines the absolute path to the project's root folder 
      based on the current file's location, ensuring consistency across different 
      operating systems and environments.

      Components:
         - __file__: A magic variable that holds the path of the script being executed.
         - Path(__file__): Converts the path string into a robust Path object from 'pathlib'.
         - .resolve(): 
            1. Converts the path from relative to absolute (Canonical Path).
            2. Resolves any symbolic links (Symlinks).
            3. Normalizes the path by removing redundant segments like '..' or '.'.
         - .parent.parent: Navigates two levels up in the directory hierarchy to reach the root.

      Returns:
         Path: A pathlib.Path object representing the full, absolute path to the project root.
      """

    
      self.root_dir = Path(__file__).resolve().parent.parent
      self.file_dir = Path(self.root_dir / "assets" / "files")
      self.file_dir.mkdir(parents=True, exist_ok=True)
   
   def generate_random_string(self, length = 12):
      return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))