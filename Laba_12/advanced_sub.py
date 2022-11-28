#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно выполнить замену, а следом
# после стрелки (--->) указан результат замены

# aAc   ---> a!A!c
# aZc   ---> a!Z!c
# aZZc  ---> a!Z!!Z!c
# aBaCa ---> a!B!a!C!a
REGEXP_1 = '([A-Z])'   # регулярное выражение
REGEXP_1_REPL = r'!\1!' # выражение для строки замены

# abc    ---> abc
# abbc   ---> abc
# azzzc  ---> azc
# arrrrc ---> arc
# xxxxxx ---> x
REGEXP_2 = r'(\w)\1+' 
REGEXP_2_REPL = r'\1'

# this is text         ---> this is text
# this is is text      ---> this *is* text
# this is is is text   ---> this *is* text
# this is text text    ---> this is *text*
# this is is text text ---> this *is* *text*
REGEXP_3 = r'(\b[a-z]+)(?=\s)(?=(\s\1))\2+' 
REGEXP_3_REPL = r'*\1*'

# one two three ---> two one three
# dog cat wolf  ---> cat dog wolf
# goose car rat ---> goose rat car
REGEXP_4 = r'(\b[a-z]{3})\s(\b[a-z]{3})' 
REGEXP_4_REPL = r'\2 \1'

# cat dog                     ---> cat dog
# cat dog cat                 ---> cat dog cat
# dog cat dog cat cat         ---> dog dog
# dog cat dog rat rat cat cat ---> dog dog rat rat
REGEXP_5 = r'(?=(\s(cat|wolf)))(?<!(^cat dog))\1' 
REGEXP_5_REPL = ''
