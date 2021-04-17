from os import path

fileName = 'data.txt'

if not path.exists(fileName):
  print('file does not exist')

try:
 n = 10/1
 print('n = ', n)

 with open(fileName) as file:
  print(file.readLines())

except ZeroDivisionError as e:
 print('Invalid operation', e)
except FileNotFoundError as e:
 print('File is not found', e)
except (ZeroDivisionError, FileNotFoundError) as e:
 print('Operation Error', e)
except Exception as e:
 print('Something went wrong', e)
finally:
 print('Please try again later')
