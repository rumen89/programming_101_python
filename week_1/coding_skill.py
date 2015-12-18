# The problem where you analyze the given json with data and
# returns some results.
#
# You have a data.json file in this repo. It is full with people objects.
# Every person have ``skills`` array with languages objects in it.
# Every skill has name and level.
#
# Write a program that does two things:
# - Read data.json file as an argument in the console.
# - Prints all languages and the best person in every language.

import json
import sys


def sort_by_lang(dict):
    result = {}
    for people in dict:
        for person in dict[people]:
            name = person['first_name'] + ' ' + person['last_name']
            for skill in person['skills']:
                name_and_level = {}
                name_and_level[name] = skill['level']
                if skill['name'] in result:
                    result[skill['name']].update(name_and_level)
                else:
                    result[skill['name']] = name_and_level
    return result


def read_json_file(json_file):
    with open(json_file, 'r') as js:
        dict = json.load(js)

    return dict


def coding_skills(json_file):
    dict = read_json_file(json_file)

    lang_level = sort_by_lang(dict)
    the_best_programmers = {}
    max_coding_level_name = ''

    for language in lang_level:
        max_coding_level = 0
        for item in lang_level[language]:
            coding_level = lang_level[language][item]
            # print(lang_level[language][item])

            if coding_level > max_coding_level:
                max_coding_level = coding_level
                max_coding_level_name = item

        the_best_programmers[language] = max_coding_level_name

    return the_best_programmers


def main():
    json_file = sys.argv[1]

    for lang in coding_skills(json_file):
        print(lang + ' - ' + coding_skills(json_file)[lang])


def people_skills(the_dict):

    lang = {}

    for people in the_dict:
        for human in the_dict[people]:
            # print(human['first_name'])
            name = human['first_name'] + ' ' + human['last_name']
            for skill in human['skills']:
                man = {}
                man[name] = skill['level']
                if skill['name'] not in lang:
                    lang[skill['name']] = man
                else:
                    lang[skill['name']].update(man)
                print("this: {} end".format(lang))

    return lang


# def coding_skill(dict):
#     for man in dict:
#         for language in dict[man]:
#


# def main():
#     file = sys.argv[1]

#     with open(file) as data:
#         the_dict = json.load(data)

#     print(people_skills(the_dict))


if __name__ == '__main__':
    main()
