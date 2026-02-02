#The third person singular verb form in English is distinguished by the suffix -s, which is added to the stem of the infinitive form: run -> runs. 
# A simple set of rules can be given as follows:

#If the verb ends in y, remove it and add ies
#If the verb ends in o, ch, s, sh, x or z, add es
#By default just add s

def third_person_singular(verb):
    if verb.endswith('y'):
        return verb[:-1] + 'ies'
    elif verb.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):
        return verb + 'es'
    else:
        return verb + 's'
