from polyglot.text import Text
import spacy

# Instantiate the English model: nlp
nlp = spacy.load('fr')

article = "édition abonné. Dans une tribune au « Monde », l’universitaire Charles Cuvelliez estime que le fantasme d’un remplacement de l’homme par l’algorithme et le robot repose sur un malentendu. Le Monde | 10.05.2017 à 06h44 • Mis à jour le 10.05.2017 à 09h47 | Par Charles Cuvelliez (Professeur à l’Ecole polytechnique de l'université libre de Bruxelles) TRIBUNE. L’usage morbide, par certains, de Facebook Live a amené son fondateur à annoncer précipitamment le recrutement de 3 000 modérateurs supplémentaires. Il est vrai que l’intelligence artificielle (IA) est bien en peine de reconnaître des contenus violents, surtout diffusés en direct.Le quotidien affreux de ces modérateurs, contraints de visionner des horreurs à longueur de journée, mériterait pourtant qu’on les remplace vite par des machines !L’IA ne peut pas tout, mais là où elle peut beaucoup, on la maudit, accusée de détruire nos emplois, de remplacer la convivialité humaine. Ce débat repose sur un malentendu.Il vient d’une définition de l’IA qui n’a, dans la réalité, jamais pu être mise en pratique : en 1955, elle était vue comme la création de programmes informatiques qui, quoi qu’on leur confie, le feraient un jour mieux que les humains. On pensait que toute caractéristique de l’intelligence humaine pourrait un jour être si précisément décrite qu’il suffirait d’une machine pour la simuler. Ce n’est pas vrai. Angoisses infondées. Comme le dit un récent Livre blanc sur la question (Pourquoi il ne faut pas avoir peur de l’Intelligence arti­ficielle, Julien Maldonato, Deloitte, mars 2017), rien ne pourra remplacer un humain dans sa globalité. L’IA, c’est de l’apprentissage automatique doté d’un processus d’ajustement de modèles statistiques à des masses de données, explique l’auteur. Il s’agit d’un apprentissage sur des paramètres pour lesquels une vision humaine n’explique pas pourquoi ils marchent si bien dans un contexte donné. C’est aussi ce que dit le rapport de l’Office parlementaire d’évaluation des choix scientifiques et technologiques (« Pour une intelligence artificielle maîtrisée, utile et démystifiée », 29 mars 2017), pour qui ce côté « boîte noire » explique des angoisses infondées. Ethiquement, se fonder sur l’IA pour des tâches critiques sans bien comprendre le comment..."

# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)

# Print the type of each entity
print(type(ent))

# Create the list of tuples: entities
entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]
entitiesPo = [ent for ent in txt.entities]

# Print the entities
print(entities)
print(entitiesPo)

# Initialize the count variable: count
count = 0

# Iterate over all the entities
for ent in txt.entities:
    # Check whether the entity contains 'Bruxelles'
    if 'Bruxelles' in ent:
        # Increment count
        count += 1

# Print count
print(count)

# Calculate the percentage of entities that refer to "Bruxelles": percentage
percentage = count * 1.0 / len(txt.entities)
print(percentage)

# Create a set of spaCy entities keeping only their text: spacy_ents
spacy_ents = {e.text for e in nlp(article).ents}
print(spacy_ents)

ttt = {'Livre', 'Monde |', 'Deloitte', 'Office', 'Charles Cuvelliez', 'Angoisses', 'Facebook Live'}

# Create a set of the intersection between the spacy and polyglot entities: ensemble_ents
ensemble_ents = spacy_ents.intersection(spacy_ents, ttt)

# Print the common entities
print(ensemble_ents)

# Calculate the number of entities not included in the new ensemble set of entities: num_left_out
num_left_out = len(spacy_ents.union(ttt)) - len(ensemble_ents)
print(num_left_out)
