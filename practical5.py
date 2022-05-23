import random

print("BOT: What do you want me to call you?")
user_name = input()

bot_template = "BOT : {0}"
user_template = user_name + " : {0}"

name = "Doctorify" 
# weather = "rainy" 
# mood = "Happy"
responses = { 
    
"what's your name?": 
[ 
"They call me {0}".format(name), 
"I usually go by {0}".format(name), 
"My name is the {0}".format(name) 
],
"how are you?":
[
    "I am full of 0 and 1's \n"
],
"how can you help me?":
[
  "I can :\n\t1)inform you remedys.\n\t2)inform you about visiting hours.\n\t"  
],
    
"what is the remedy for cold?": 
[ 
"1. You can take steam twice a day \n      2. You can apply vicks on your chest and nose \n      3. Drink warm water\n"
],

"what are the medicines for cold?": 
[ 
"1. D Cold Total twice a day \n      2. Sinarest once a day \n"
],
    
"what is the remedy for sore throat?": 
[ 
"1. You can gargle with warm water and salt thrice a day \n      2. Sip herbal teas \n      3. Drink warm water\n"
],

"what are the medicines for sore throat?": 
[ 
"1. Strepsils twice a day \n      2. ThroatCalm twice a day\n"
],
    
"what is the remedy for fever?": 
[ 
"1. Keep putting cold strips on your head \n      2. Keep yourself hydrated \n      3. Take a lukewarm water bath\n"
],

"what are the medicines for fever?": 
[ 
"1. Crocin twice a day \n      2. Dolo650 twice a day\n"
],
    
"what is the remedy for stomach ache?": 
[ 
"If you are having an upset stomach you should: \n\t 1. Eat light food and drink lots of water \n\t 2. Have curd\n\t 3. Have a bread toast if you are having loose motions\n" 
"      If you feel bloated : \n\t 1. Have peppermint tea \n\t 2. Take a walk\n\t 3. Drink lots of water\n  "

],

"what are the medicines for stomach ache?": 
[ 
"If you are having an upset stomach you can take: \n\t 1. NorfloxTZ twice a day \n\t 2. Digene twice a day\n"  
"      If you feel bloated you can take: \n\t 1. Pudin Hara Liquid twice a day \n\t 2. Imodium twice a day\n "
],
"visiting hours":
[
    "You can vist between 8:00 am to 8:00 pm.\n"
],
"Are you a robot?": [ 
"What do you think?", 
"Maybe yes, maybe no!", 
"Yes, I am a robot with human feelings.", ],
# "how are you?": [ 
# "I am feeling {0}".format(mood), 
# "{0}! How about you?".format(mood), 
# "I am {0}! How about yourself?".format(mood), ],
"": [ 
"Hey! Are you there?", 
"What do you mean by saying nothing?", 
"Sometimes saying nothing tells a lot :)", ],
"default": [
"this is a default message"] }

def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message
def related(x_text): #keyword
    if "name" in x_text: 
        y_text = "what's your name?"
    elif "help" in x_text: 
        y_text = "how can you help me?"
    elif "cold" in x_text and "remedy" in x_text: 
        y_text = "what is the remedy for cold?"
    elif "cold"in x_text and "medicine" in x_text: 
        y_text = "what are the medicines for cold?"
        
    elif "sore throat" in x_text and "remedy" in x_text: 
        y_text = "what is the remedy for sore throat?"
    elif "sore throat" in x_text and "medicine" in x_text: 
        y_text = "what are the medicines for sore throat?"
        
    elif "fever"  in x_text and "remedy" in x_text:
        y_text = "what is the remedy for fever?"
    elif "fever" in x_text and "medicine" in x_text: 
        y_text = "what are the medicines for fever?"
        
    elif "stomach ache"  in x_text and "remedy" in x_text:
        y_text = "what is the remedy for stomach ache?"
    elif "stomach ache" in x_text and "medicine" in x_text: 
        y_text = "what are the medicines for stomach ache?"
    elif "visiting" in x_text:
        y_text="visiting hours"    
    elif "robot" in x_text: 
        y_text = "Are you a robot?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    else: 
        y_text = ""
    return y_text

def send_message(message): 
  print(user_template.format(message)) 
  response = respond(message) 
  print(bot_template.format(response))

while 1: 
  my_input = input() 
  my_input = my_input.lower() 
  if my_input == "exit" or my_input == "stop" or my_input == "bye": 
    break
  related_text = related(my_input) 
  send_message(related_text)
  

