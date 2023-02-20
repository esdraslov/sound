import playsound

def playMP3(adress):
  if ".mp3" in adress:
    playsound("./" + adress)
  else:
    print("TypeError: \n")
    print(adress + " is not allowed")

def playWAV(adress):
  if ".wav" in adress:
    playsound("./" + adress)
  else:
    print("TypeError: \n")
    print(adress + " is not allowed")