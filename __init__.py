import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # add root module to sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))  # add src module to sys.path

from src import run

run()
