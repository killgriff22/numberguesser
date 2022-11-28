import random,os
listmaster=[]
listguesses=[]
wrong=0
wrongtotal=0
wrongindexes=[]
cycles=0
def weight():
  return int(random.random()*15)+1
size=20
magnitude=100
for i in range(size):
  listmaster.append(int(random.random()*magnitude))
  listguesses.append(int(random.random()*magnitude))
def check_answers():
  global wrong,wrongtotal
  for i in range(len(listmaster)):
    print(listguesses[i],listmaster[i])
    print(listguesses[i] == listmaster[i])
    if listguesses[i] != listmaster[i]:
      wrong+=1
      wrongtotal+=1
      wrongindexes.append(i)
  if wrong==0:
    print("FINISH")
    print(wrongtotal)
    return True
  else:
    wrong=0
    return False
def generate_new_guesses():
  print("RETRY")
  global wrong
  for index in wrongindexes:
    if listguesses[index] >=magnitude or listguesses[index]<0:
      listguesses[index]=0
    if listguesses[index] != listmaster[index]:
      upordown = int(random.random()*2)
      if upordown == 0 :
        listguesses[index] -= weight()
      elif upordown == 1:
        listguesses[index] += weight()
  os.system("clear")
while True:
  while not check_answers():
      generate_new_guesses()
  with open("log.txt","a") as log:
    log.write(f"{wrongtotal}\n")
  if cycles % 1000 == 0 and not cycles==0:
    with open("log.txt","r") as log:
      items = log.read().split("\n")
      last_item = items[len(items) - 1]
      last_item = items.pop() 
      average=0
      for item in items:
        average+=int(item)
    average=average/len(items)
    with open("log2.txt","a") as log:
      log.write(f"{cycles},{average}\n")
  wrongtotal=0
  listmaster=[]
  for i in range(size):
    listmaster.append(int(random.random()*100))
  cycles+=1