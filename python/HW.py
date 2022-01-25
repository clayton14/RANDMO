import wikipedia, os, sys, random

#TODO : make a more well rounded web scraping tool 
# add GUI maye
# add google docs support


def main(search_terms, num_sentance, output="out.txt"):

    with open(os.path.join(os.getcwd(), output), 'r+') as f:
        for i in range(len(search_terms)):
            r = wikipedia.summary(search_terms[i], sentences=num_sentance)   
            f.writelines(search_terms[i] + " : " +  r + "\n\n\n")
            print("DONE: " + search_terms[i])
        f.close()
        print("=====research complete=====")

#listh of this to to look up example x = ["minecraft", "Jacob Riis"]
x = ['Jacob Riis']


main(x, 3, output="out.txt")
