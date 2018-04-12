import csv
from pydub import AudioSegment
from pydub.playback import play
from sklearn import tree


def provjeriDaNe():
    while True:
        x = input()
        if x.lower() == "da":
            return 1
        elif x.lower() == "ne":
            return 0
        else:
            print("Niste upisali ispravnu vrijednost")

def provjeriUIntervalu(donji, gornji):
    while True:
        x = input()
        try:
            x = int(x)
        except:
            print("Niste unijeli broj. Unesite ponovno")
        else:
            if x >= donji and x <= gornji:
                return x - 1
            else:
                print("Niste unijeli broj u mogucem intervalu. Unesite ponovo")


X = []
y = []
with open('pusenje.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        row = list(map(int, row))
        X.append(row[0:4])
        y.append(row[4])

clf = tree.DecisionTreeClassifier()

clf.fit(X, y)

print("Koji dan? (1 za ponedjeljak - 7 za nedjelju)")
x1 = provjeriUIntervalu(1, 7)
if x1 == 6:
    x1 = 5

print("Koji sat? (1 - 7)")
x2 = provjeriUIntervalu(1, 7)

print("Je li imao para? (Da/Ne)")
x3 = provjeriDaNe()

print("Je li imao pljugi? (Da/Ne)")
x4 = provjeriDaNe()

test = (x1, x2, x3, x4)

predictions = clf.predict([test])
if test[3] == 0 and predictions[0] == 1:
    jesi = AudioSegment.from_mp3('./Jane_jesi_kratak.mp3')
    play(jesi)
    print("Jane, jesi kratak")
elif predictions[0] == 1:
    print("Pusio je svoje pljuge")
else:
    nije = AudioSegment.from_mp3('./Nije_pusio.mp3')
    play(nije)
    print("Nije pusio")

import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("karlo")

#pip3 install sklearn scipy numpy graphviz pygame pydub
#dan, sat, jel ima para, jel ima pljugi, jel zapalio
#https://github.com/machine-learning-projects/machine-learning-recipes
#http://scikit-learn.org/stable/modules/tree.html#tree-classification
#https://en.wikipedia.org/wiki/Decision_tree_learning
#sudo apt-get install graphviz
#sudo apt-get install ffmpeg
#https://www.google.hr/search?ei=5S7FWtuGKszMwALPibPACQ&q=google+machine+learning+recipes&oq=google+machine+learning+rec&gs_l=psy-ab.3.0.35i39k1j0i22i30k1.1895.2516.0.3580.4.4.0.0.0.0.238.560.0j2j1.3.0....0...1c.1.64.psy-ab..1.3.559...0j0i67k1.0.a3lB8JmyQ0M