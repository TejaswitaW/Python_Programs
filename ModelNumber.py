# Get the model number.
model = int(input('Enter the model number: '))
# Validate the model number.
while model != 100 and model != 200 and model != 300 and model !=500:
    print('The valid model numbers are 100, 200 and 300.')
    model = int(input('Enter a valid model number: '))
