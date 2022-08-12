"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    villager_data=open(filename)
    species = set()
    for line in villager_data:
        new_line=line.split("|")
        species_type= new_line[1]
        species.add(species_type)


    

    # TODO: replace this with your code 

    return species

# print(all_species("villagers.csv"))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    villagers = []
    villager_data = open(filename)
    for line in villager_data:
        new_line = line.split('|')
        if search_string == new_line[1]:
            villagers.append(new_line[0])
        elif search_string == "All":
            villagers.append(new_line[0])

    # TODO: replace this with your code

    return sorted(villagers)

#print(get_villagers_by_species('villagers.csv', search_string = 'Dog'))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    villager_data = open(filename)
    fitness_list = []
    nature_list = []
    education_list = []
    music_list = []
    fashion_list = []
    play_list = []
    for line in villager_data:
        new_line = line.split("|")
        name = new_line[0]
        hobby = new_line[3]
        if hobby == "Fitness":
            fitness_list.append(name)
        elif hobby == "Nature":
            nature_list.append(name)
        elif hobby == "Education":
            education_list.append(name)
        elif hobby == "Music":
            music_list.append(name)
        elif hobby == "Fashion":
            fashion_list.append(name)
        elif hobby == "Play":
            play_list.append(name)


    return [sorted(fitness_list), sorted(nature_list), sorted(education_list), sorted(music_list), sorted(fashion_list), sorted(play_list)]
    
print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
