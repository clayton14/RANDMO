import wikipedia, os, sys, random
from wikipedia import PageError
from wikipedia import DisambiguationError
#TODO : make a more well rounded web scraping tool 
# add GUI maye
# add google docs support


def main(search_terms, num_sentance, output="out.txt"):
    with open(os.path.join(os.getcwd(), output), 'r+') as f:
        try:
            for i, term  in enumerate(search_terms):
                searchs = wikipedia.search(term)
                for search in searchs:
                    summary = wikipedia.summary(search, sentences=num_sentance)
                    f.writelines(term + ": " + summary + "\n\n\n")
                    print("DONE: " + search)
        except PageError and DisambiguationError as e:
            print(e)
            print(f"[ERROR] {term}, searching for related information")

        print("=====research complete=====")
    
            

def search_test():
    x = wikipedia.search("J.P. Morgan")
    print(x)
    for i, terms in enumerate(x):
        print(wikipedia.summary(terms), end='\n')


def test(search_terms, num_sentance, output="out.txt"):
    num_terms = len(search_terms) 
    while num_sentance > 0:
        try:
            wikipedia.summary(search_terms[num_sentance])
            num_terms -= 1
            print("DONE: " + search_terms[num_sentance])
        except PageError as e:
            print(f"[ERROR] could not find page for {search_terms[num_terms]}")
            print(e)
            num_terms -= 1

        print("=====research complete=====")

#listh of this to to look up example x = ["minecraft", "Jacob Riis"]
# x = [ 
# "Edward Bellamy","Suburban", "steel frame", "sprawl", "public transit", "Great Wave", 
# "collective bargaining", "strike", "union", "Robber Baron", "strike breaker", 
# "zoning", "postindustrial", "load bearing masonry", "Otis safety brake", "May Day", 
# "Homestead Strike", "Pullman Strike", "Pullman Porters"
# ]

x = [
    "Edward Bellamy","Suburban", "steel frame", "sprawl", "public transit", "Great Wave", 
]
test(x, 3, output="out.txt")
#earch_test()