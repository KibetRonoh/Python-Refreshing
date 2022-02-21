# what is the output of the following code?
f = None
for i in range(5):
    with open('app.log', 'w') as f:
        if i > 2:
            break

print(f.clossed)

#true