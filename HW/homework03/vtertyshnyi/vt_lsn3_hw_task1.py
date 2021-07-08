row_splitter = '\n' + '#' * 100 + '\n'

zen = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

words_to_count = ('better', 'never', 'is')

print(row_splitter)
print(f"PART 1 => Amount of words:")
for word in words_to_count:
    print(f"\t- \"{word}\": {zen.count(word)}")
print(row_splitter)

print(row_splitter)
print("PART 2 => Print Zen in uppercase:")
print(zen.upper())
print(row_splitter)

print(row_splitter)
print(f"PART 3 => Replace all 'i' charachters with '&':")
print(zen.replace('i','&'))
print(row_splitter)
