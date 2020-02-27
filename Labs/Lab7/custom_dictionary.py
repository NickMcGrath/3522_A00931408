import difflib
from datetime import datetime

"""
This module loads a txt file full of definitions and terms, asks the user 
what they want to query, and saves the queries to and output txt file.
"""


class WordNotFoundError(Exception):
    """
    WordNotFoundError is thrown when a word can not be found in the
    CustomDictionary terms.
    """

    def __init__(self, missing_word):
        """
        Initialize the error and set the word that caused the error.
        :param missing_word the word that caused the error
        """
        super().__init__()
        self.missing_word = missing_word


class CustomDictionary:
    """
    CustomDictionary loads a txt file with terms and definitions and
    provides methods to work on the definitions.
    """

    def __init__(self, path):
        """
        Initialize the CustomDictionary.
        :param path: path to file containing definitions and terms
        """
        with open(path, mode='r', encoding='utf-8') as definitions_file:
            def_file = definitions_file.read()
            split_def_file = def_file.split('--')
            self.definitions = {d.split('\n').pop(0): d.split('\n')[1:-1]
                                for d in split_def_file}
            self.queries = []

    def words_queried(self, word):
        """
        Keeps track of words that where queried.
        :param word: string
        """
        if word not in self.queries:
            self.queries.append(word)

    def query(self, word):
        """
        Query the definitions with the term.
        :param word: term
        :return: list of sentances defining the term
        """
        word = word.lower()
        fixed_word = difflib.get_close_matches(word,
                                               self.definitions.keys(),
                                               n=1)
        if len(fixed_word) <= 0:
            raise WordNotFoundError(word)
        self.words_queried(fixed_word[0])
        return self.definitions[fixed_word[0]]

    def export(self):
        """
        Export the terms queried with there definitions in a txt file.
        """
        with open('word_queries.txt', mode='a', encoding='utf-8') as \
                export_file:
            # export_file.write(
            #     '\n' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
            for definition in self.queries:
                export_file.write('\n--' + definition)
                for description in self.definitions[definition]:
                    export_file.write('\n' + description)


def main():
    """
    Main method, creates a CustomDictionary and then prompts the user
    for what terms they want to see, saves the queries to txt file.
    :return: int
    """
    c = CustomDictionary('data.txt')
    while True:
        try:
            word = input('Query a word my dude (or enter 1 to exit):')
            if word == '1':
                break
            for sentance in c.query(word):
                print(sentance)
        except WordNotFoundError as e:
            print(e.missing_word + " is not in the definitions")
        else:
            pass
        finally:
            pass

    c.export()


if __name__ == '__main__':
    main()
