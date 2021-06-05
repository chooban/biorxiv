import sys
from biorxiv import search

def main(argv):
  results = [] * len(argv)
  
  for url in argv:
    result = search(url)
    results.append(result)

  for r in results:
    print(r[0],"\t",r[1],"\t",r[2])  

if __name__ == "__main__":
    main(sys.argv[1:])
