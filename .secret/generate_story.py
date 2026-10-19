filename = 'madlibs.txt'
story = '''
Our new pitch to prospective GVSU students:

Welcome to GVSU! We are a {} university located in Allendale, Michigan. Allendale is a {} town, with a population of 26,000 {}. Our university offers {} majors, spread across various departments and {}. 

Life at GV is {}! We have many student organizations, ranging from {} appreciation club to an intramural {} team. Living on campus is great, too! Most of our dorms are fairly {}. They even have {}! Just hope you don't get stuck with a {} roommate! 

You'd love it here! We hope you choose to be a GVSU {}!
'''

word_list = []
with open(filename, 'r') as fp:
  for line in fp:
    line = line.strip()
    if line == '':
      continue
    line_parts = line.split(':')
    if len(line_parts) < 2:
      print('Error! Missing colon (:) in line:')
      print(line)
      print('Exiting...')
      quit(1)
    word = ':'.join(line_parts[1:])
    word = word.strip()
    if len(word) == 0:
      print('Error! No word given on line:')
      print(line)
      print('Exiting...')
      quit(2)
    word_list.append(word)
if len(word_list) != 12:
  print('Error! I expected exactly 12 words.')
  print('Your ' + filename + ' had ' + str(len(word_list)))
  print('Please fix this and try again, maybe you added or deleted a line?')
  quit(1)
 
      
print(story.format(*word_list))

