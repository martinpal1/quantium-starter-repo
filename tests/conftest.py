import os
import sys
from pathlib import Path

from webdriver_manager.chrome import ChromeDriverManager


ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

chromedriver_path = ChromeDriverManager().install()
chromedriver_dir = str(Path(chromedriver_path).parent)

os.environ["PATH"] = chromedriver_dir + os.pathsep + os.environ["PATH"]