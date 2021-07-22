# Записати в стрічку філософію Пайтона
# Знайти в заданій стрічці кількість входжень слів (better, never, is)
# Вивести весь текст у верхньому регістрі (всі великі літери)
# Замінити всі входження символу “і” на “&”

# кількість входжень слів
philosophy = ('\n'
              'Beautiful is better than ugly.\n'
              'Explicit is better than implicit.\n'
              'Simple is better than complex.\n'
              'Complex is better than complicated.\n'
              'Flat is better than nested.\n'
              'Sparse is better than dense.\n'
              'Readability counts.\n'
              'Special cases aren\'t special enough to break the rules.\n'
              'Although practicality beats purity.\n'
              'Errors should never pass silently.\n'
              'Unless explicitly silenced.\n'
              'In the face of ambiguity, refuse the temptation to guess.\n'
              'There should be one-- and preferably only one --obvious way to do it.\n'
              'Although that way may not be obvious at first unless you\'re Dutch.\n'
              'Now is better than never.\n'
              'Although never is often better than *right* now.\n'
              'If the implementation is hard to explain, it\'s a bad idea.\n'
              'If the implementation is easy to explain, it may be a good idea.\n'
              'Namespaces are one honking great idea -- let\'s do more of those! """\n'
              'number_of_words = len(philosophy.find(\'better\',\'never\',\'is\')) ')
text = ['better', 'never', 'is']
word = 0
while word < len(text):
    print('Word', text[word], 'is used', philosophy.count(text[word]), 'times')
    word += 1
# текст у верхньому регістрі
print(philosophy.upper())
# символ “і” на “&”
philosophyReplace = philosophy.replace('i', '&')
print(philosophyReplace)



