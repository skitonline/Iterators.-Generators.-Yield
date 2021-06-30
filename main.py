import hashlib
from WikipediaCountriesIter import WikipediaCountriesIter


def generator_hash_md5(file):
    with open(file, 'r') as f:
        for line in f:
            hash_object = hashlib.md5(line.encode())
            yield hash_object.hexdigest()


def main():
    wiki = WikipediaCountriesIter()
    with open('output.txt', 'w', encoding='utf-8') as f:
        for el in wiki:
            f.write(el)
            f.write('\n')
    for hash in generator_hash_md5('output.txt'):
        print(hash)


if __name__ == '__main__':
    main()

