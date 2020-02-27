import re
import keyword
import difflib
from datetime import date, datetime


class WordNotFoundError(Exception):
    def __init__(self, missing_word):
        super().__init__()
        self.missing_word = missing_word


class CustomDictionary:
    def __init__(self, path):
        # self.definitions = {}
        with open(path, mode='r', encoding='utf-8') as definitions_file:
            def_file = definitions_file.read()
            split_def_file = def_file.split('--')
            self.definitions = {d.split('\n').pop(0): d.split('\n')[1:] for d
                                in split_def_file}
            self.queries = []
            print(self.definitions)

    def words_queried(self, word):
        if word not in self.queries:
            self.queries.append(word)

    def query(self, word):
        word = word.lower()
        fixed_word = difflib.get_close_matches(word,
                                               self.definitions.keys(),
                                               n=1)
        if len(fixed_word) <= 0:
            raise WordNotFoundError(word)
        self.words_queried(fixed_word[0])
        return self.definitions[fixed_word[0]]

    def export(self):
        with open('word_queries.txt', mode='a', encoding='utf-8') as \
                export_file:
            export_file.write(
                '\n' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
            for definition in self.queries:
                export_file.write('--' + definition)
                for description in self.definitions[definition]:
                    export_file.write('\n' + description)


def main():
    c = CustomDictionary('data.txt')
    while True:
        try:
            word = input('Query a word my dude (or enter 1 to exit):')
            if word == '1':
                break
            print(c.query(word))
        except WordNotFoundError as e:
            print(e.missing_word + " is not in the definitions")
        else:
            pass
        finally:
            pass

    c.export()


if __name__ == '__main__':
    main()
