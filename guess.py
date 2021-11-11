#!/usr/bin/env python3

print("Myslim si cislo od 1 do 20")
secret = 7
tip = None
counter = 5

while counter >= 0 and secret != tip:
     tip = input("Tvoj tip: ")
     tip = int(tip)

     if tip < secret:
          print("Hmm... Moje cislo je vacsie ako tvoje")
          counter -= 1
     elif tip > secret:
          print("Hmmm... Moje cislo je mensie ako tvoje")
          counter -= 1
     else:
           print("Hmmm... ta ty genius")
           break
else:
     print(f"Ta ty si lama! Moje tajne cislo je {secret}.")

print("Good bye. ")













