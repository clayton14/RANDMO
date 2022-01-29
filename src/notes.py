import wikipedia
import os
import sys
import random
from wikipedia import PageError
from wikipedia import DisambiguationError
import warnings
# TODO : make a more well rounded web scraping tool
# add GUI maye
# add google docs support


def main(search_terms, num_sentance, output="out.txt"):
    assert len(search_terms) != 0, "List is empty"
    warnings.catch_warnings()
    warnings.simplefilter("ignore")
    with open(os.path.join(os.getcwd(), output), "w+") as f:
        for term in search_terms:
            try:
                summary = wikipedia.summary(term, sentences=num_sentance)
                print(f"[DONE]: {term}")
                f.writelines(f"{term}:\n{summary}\n\n")
            except PageError as e:
                print(
                    f"[ERROR:{term}] page not found for {term}! try and make your search terms more specific\n")
                continue
            except DisambiguationError as e:
                print(
                    f"[ERROR:{term}] multple things are related to {term}.\nDid you mean{e.options}")


                # listh of this to to look up example x = ["minecraft", "Jacob Riis"]
# x = [
#     "Edward Bellamy", "Suburban", "steel frame", "sprawl", "public transit", "Great Wave",
#     "collective bargaining", "strike", "union", "Robber Baron", "strike breaker",
#     "zoning", "postindustrial", "load bearing masonry", "Otis safety brake", "May Day",
#     "Homestead Strike", "Pullman Strike", "Pullman Porters"
# ]
x = [
    "sprawl", "Edward Bellamy", "Suburban", "steel frame", "Urban sprawl", "public transit",
]
main(x, 3, output="out.txt")
# earch_test()
