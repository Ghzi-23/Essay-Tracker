text = """
Roar!
Tipe, tipe, zangalewa (World Cup! World Cup!)
Tipe, tipe, zangalewa (World Cup! World Cup!)
Tipe, tipe, zangalewa (World Cup! World Cup!)
Tipe, tipe, zangalewa (World Cup! World Cup!)
You're a good soldier, choosing your battles
Pick yourself up and dust yourself off, get back in the saddle
You're on the frontline, everyone's watching
You know it's serious, we're getting closer, this isn't over
The pressure's on, you feel it
But you got it all, believe it
When you fall get up, oh, oh
And if you fall get up, eh, eh
Tsamina mina zangalewa 'cause this is Africa
Tsamina mina, eh, eh
Waka waka, eh, eh
Tsamina mina zangalewa
This time for Africa
Listen to your God, this is our motto
Your time to shine, don't wait in line, y vamos por todo
People are raising their expectations
Go on and feed them, this is your moment, no hesitation
Today's your day, I feel it
You paved the way, believe it
If you get down get up, oh, oh
When you get down get up, eh, eh
Tsamina mina zangalewa
This time for Africa
Tsamina mina, eh, eh
Waka waka, eh, eh
Tsamina mina zangalewa, anawa-a-a
Tsamina mina, eh, eh
Waka waka, eh, eh
Tsamina mina zangalewa
This time for Africa
Abuyile amajoni pikipiki mama, one A up to Z
Bathi susa lamajoni pikipiki mama from East to West
Bathi waka waka mah eh, eh
Waka waka mah eh, eh
Zonk' iZizwe masibuye 'cause this is Africa (Africa, Africa...)
Tsamina mina, anawa-a-a
Tsamina mina
Tsamina mina, anawa-a-a
"""

word_count = {}

for word in text.lower().split():
   if word in word_count:
        word_count[word] += 1 
   else:
        word_count[word] = 1

print(word_count)