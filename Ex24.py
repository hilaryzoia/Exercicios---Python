#first and last occurrence of a string

phrase = str(input('Enter a phrase: ')).upper().strip()
print('The letter A appears {} times in the sentence'.format(sentence.count('A')))
print('The first letter A appeared in position {}'.format(phrase.find('A')+1))
print('The last letter A appeared in position {}'.format(phrase.rfind('A')+1))
