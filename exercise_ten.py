digitalnumber = int(input('Enter a three digital number'))
firstnumber = digitalnumber // 100
secondnumber = digitalnumber % 100 // 10
thridnumber = digitalnumber % 10
sum = firstnumber + secondnumber + thridnumber
average = sum / 3
product = firstnumber + secondnumber + thridnumber
print('The sum is', firstnumber, secondnumber, thridnumber, 'is ', sum)
