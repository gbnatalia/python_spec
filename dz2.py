'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или документации к языку.
'''
import string
import re
from collections import Counter

def handler_text(text:str) -> None:
    # замена всякой пунктуации на пробелы, избавление от 2йных пробелов, приведение к нижнему регистру
    for item in string.punctuation:
        text = text.replace(item, " ")
    text = text.replace("—", " ").replace("\n", " ").replace("   ", " ").lower()

    # подсчет слов с помощью Counter
    wordcount = Counter(text.split())

    # вывод 10 самых встречаемых слов
    for word, count in wordcount.most_common(10):
        print(f"{word:<20} - {count:<}")

if __name__ == "__main__":
    text = '''
Python (в русском языке встречаются названия питон или пайтон) — 
высокоуровневый язык программирования общего назначения с динамической строгой типизацией и 
автоматическим управлением памятью, ориентированный на повышение производительности разработчика, 
читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. 
Язык является полностью объектно-ориентированным в том плане, что всё является объектами. 
Необычной особенностью языка является выделение блоков кода пробельными отступами. 
Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. 
Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. 
Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных 
на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++.
Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, 
объектно-ориентированное программирование, метапрограммирование и функциональное программирование. 
Задачи обобщённого программирования решаются за счёт динамической типизации. 
Аспектно-ориентированное программирование частично поддерживается через декораторы, 
более полноценная поддержка обеспечивается дополнительными фреймворками. 
Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. 
Основные архитектурные черты — динамическая типизация, автоматическое управление памятью, полная интроспекция, 
механизм обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL), 
высокоуровневые структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, 
могут объединяться в пакеты.
'''
    handler_text(text)