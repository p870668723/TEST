import aiml
import os
os.chdir("/home/pf/TEST/aimlTEST/aiml/")
bot = aiml.Kernel()
bot.setBotPredicate("name","BORIS")
bot.learn('std-srai.aiml')
while True:
    print bot.respond(raw_input("Enter input >"))
