# Dijkstra_Search_word
A simple project developed during the Algorythms course

### Technologies
- Python
- Django rest framework

### Purpose
Search the correlation between two words of a given dataset.<br/>This was made by applying the Dijkstra algorythm to find the shortest path that correlact the two words

### Data structure
Node
```
{
  id: int
  label: str
  value: int
}
```

### Endpoints
```
url: /api/get_way
method: POST
body: {
  sourceValue: string;
  targetValue: string;
}
returns: Node[]
```
