def hello():
  print("Greetings and salutations!")

def pack(x, y, z):
  return [x, y, z]

def eat_lunch(list):
  if len(list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(list)):
      if i == 0:
        print(f"First I eat {list[0]}")
      else:
        print(f"Next I eat {list[i]}")

hello()
lunch = pack("PB&J sandwich", "fruit roll-up", "hard-boiled egg")
print(lunch)
eat_lunch(lunch)
