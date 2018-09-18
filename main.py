from ch01.hash_map import HashMap

def main():
  map = HashMap(
    ("a", 10),
    ("b", 20),
    ("c", 30),
    ("d", 40),
  )
  print(map.get("a"))
  print(map.get("b"))
  print(map.get("c"))
  print(map.get("d"))
  print(map.get("e"))
  map.put("e", 50)
  print(map.get("e"))
  map.put("e", 51)
  print(map.get("e"))

if __name__ == "__main__":
  main()
