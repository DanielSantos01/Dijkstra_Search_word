import json

def get_data():
  file = open('dataset.json')
  data = json.load(file)
  file.close()
  return data
