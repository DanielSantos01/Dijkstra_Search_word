class List:
  def __init__(self, nodes):
    length = len(nodes)
    self.list = nodes
    self.vertex_distance = [0] * length
    self.before = [0] * length

  def __merge(self, vetor, left, middle, right):
    i = left
    j = middle + 1

    aux = vetor[::]

    for index in range(left, right + 1):
      if i > middle:
        vetor[index] = aux[j]
        j += 1
      elif j > right:
        vetor[index] = aux[i]
        i += 1
      elif aux[i]["value"] > aux[j]["value"]:
        vetor[index] = aux[j]
        j += 1
      else:
        vetor[index] = aux[i]
        i += 1

  def __top_down(self, vetor, left, right):
    if left >= right: return

    middle = (left + right) // 2
    self.__top_down(vetor, left, middle)
    self.__top_down(vetor, middle + 1, right)

    self.__merge(vetor, left, middle, right)

  def __merge_sort(self, list):
    self.__top_down(list, 0, len(list) - 1)

  def __relax(self, source, target, weight):
    if self.vertex_distance[target] > self.vertex_distance[source] + weight:
      self.before[target] = source
      self.vertex_distance[target] = self.vertex_distance[source] + weight

  def run_dijikstra(self, id):
    ordened_list = []
    resp = []

    for v in self.list:
      self.vertex_distance[v.id] = 9999999
      self.before[v.id] = -1

    self.vertex_distance[id] = 0
    for v in self.list:
      ordened_list.append({"value": self.vertex_distance[v.id], "id": v.id})
        
    while len(ordened_list) > 0:
      self.__merge_sort(ordened_list)
      current = ordened_list[0]
      ordened_list = ordened_list[1:]
      resp.append(current)
        
      for vertex in self.list[current["id"]].links:
        self.__relax(current["id"], vertex.id, 1)

  def find_connection(self, source, target):
    self.run_dijikstra(source)
    resp = [target]

    last_vertex = self.before[target]
    while last_vertex != -1:
      resp.append(last_vertex)
      last_vertex = self.before[last_vertex]

    return resp

  def search_word(self, word):
    node = None
    count = 0

    while count < len(self.list) - 1 and node == None:
      if self.list[count].label == word: node = self.list[count]   
      count += 1

    return node
    
  def find_by_id(self, id):
    node = None
    count = 0

    while count < len(self.list) - 1 and node == None:
      if self.list[count].id == id: node = self.list[count]
      count += 1

    return node

  def find_connection_label(self, word_1, word_2):
    word_1 = self.search_word(word_1)
    word_2 = self.search_word(word_2)

    if word_1 == None or word_2 == None: return []

    connections = self.find_connection(word_1.id, word_2.id)
    connections_label = []

    for id in connections:
      connections_label.append(self.find_by_id(id).label)

    return connections_label