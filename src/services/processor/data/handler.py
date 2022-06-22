import json
from pathlib import Path

def get_data():
  file = open(f'{str(Path(__file__).parent)}/dataset.json')
  data = json.load(file)
  file.close()
  return data
