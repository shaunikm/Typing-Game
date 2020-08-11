from Edit_Distance_Formula import editDistDP
import time, sys
import random

lst_of_str = ['The Ansi escape codes let you set the color of the text-background the same way it lets you set the color of the foreground.\n',
              'Matt Haig singles out LOL as one of the three most popular initialisms in Internet slang, alongside BFN ("bye for now") and IMHO ("in my honest/humble opinion"). \nHe describes the various initialisms of Internet slang as convenient, but warns that "as ever more obscure acronyms emerge they can also be rather confusing".\n'
              ]

#type_str = 'The Ansi escape codes let you set the color of the text-background the same way it lets you set the color of the foreground.\n'
type_str = random.choice(lst_of_str)
str_check = 0
a = ''
char_count = 0
mistake_count = 0

for i in type_str:
    if i != '\n':
        a += i
        char_count += 1

score_set = 100/char_count

sys.stdout.write('\r' + format('This is a typing game/test. It will test how accurately and fast you type.'))
time.sleep(5)
sys.stdout.flush()
sys.stdout.write('\r' + 'Once the game shows you the paragraph, you will have 3 seconds to read the paragraph. Get ready!')
time.sleep(5)
sys.stdout.flush()
sys.stdout.write('\r')

sys.stdout.write('\r' + format(type_str))
for i in range(1, 4):
    sys.stdout.write('\r' + str(i))
    time.sleep(1)
    sys.stdout.flush()
sys.stdout.flush()
sys.stdout.write('\r')

kl = time.time()
user_ = input('')
kp = time.time()
sys.stdout.flush()
sys.stdout.flush()
sys.stdout.write('\r')
sys.stdout.write('\rProcessing')
sys.stdout.flush()
time.sleep(0.8)
sys.stdout.write('\rProcessing.')
sys.stdout.flush()
time.sleep(0.8)
sys.stdout.write('\rProcessing..')
sys.stdout.flush()
time.sleep(0.8)
sys.stdout.write('\rProcessing...')
sys.stdout.flush()
time.sleep(1)
sys.stdout.write('\r')

mistake_count += editDistDP(user_, a, len(user_), len(a))

timel = 'Time Taken: ' + str(round(kp - kl)) + ' seconds'
if round(100 - score_set * mistake_count) >= 0:
    acc = 'Accuracy: ' + str(round(100 - score_set * mistake_count, 2)) + '%'
else:
    acc = 'Accuracy: 0.0%'
print(timel)
print(acc)