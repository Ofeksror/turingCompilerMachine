file = input("Enter the name of the (.txt) file containing the turing machine instructions: ")

raw = open(file, "r").read().replace('\n', '')

# Load data from txt into states:
data = raw.split(':')[1:-1]

States = [i for i in range(30)]

for i in range(0, len(data), 2):
    state = data[i]
    try:
        req = data[i+1].split(';')
    except Exception:
        req = None

    continues = {}

    if req == None or state[0] == 'Q':
        continues['END'] = {"Replace": "END", "Forward": "END", "Goto": "END"}
    else:
        for con in req:
            sign, replace, forward, goto = con.split(',')
            continues[sign] = {"Replace": replace, "Forward": forward, "Goto": goto}
            
    States[int(state[1:])] = continues

# Read strip from user:
userStrip = str(input("Enter strip (0 indicates empty space):\n   |- "))
# TODO: Check if strip is valid

# Loads strip
Strip = list(userStrip.ljust(20, '0'))

# Runs the machine
pos = 0
index = 0

while True:
    current = Strip[index]
    
    if (States[pos].get('END') != None):
        print("SUCCESS") # Success (ACCEPTABLE STATE, NO FURTHER INPUT)
        break
    
    if States[pos].get(current) == None:
        print(f"BROKE, state = {pos} current = {current}")
        break
    
    if (States[pos].get(current) == None):
        print(f"Broke at state {pos} with letter {current}")
        break

    Strip[index] = States[pos][current].get('Replace')
    if States[pos][current].get('Forward') == 'R':
        index += 1
    elif States[pos][current].get('Forward') == 'L':
        index -= 1
        if index < 0:
            print(f"Broke at state {pos} with index less than 0")        
            break
    elif States[pos][current].get('Forward') == 'END':
        print("Nothing to do here")
    else:
        print(f"Invalid forward movement on state {pos}")
        break

    print(f"State {pos}:   " + ''.join(Strip))
    
    pos = int(States[pos][current].get('Goto'))

print("===========\n   DONE!   \n===========")

print("OLD STRIP:   " + ' '.join(list(userStrip.ljust(40, '0'))))
print("RESULT:      " + ' '.join(Strip))