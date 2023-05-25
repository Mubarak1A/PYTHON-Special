#!/usr/bin/python3
'''This Script help check if a password have been compromise before
   and count how many times it has been compromise
'''
import requests
import hashlib
import sys


def request_api_data(query):
  '''request the api data'''
  url = 'https://api.pwnedpasswords.com/range/' + query
  res = requests.get(url)

  if res.status_code != 200:
    raise RuntimeError(
      f'Error fetching: {res.status_code}, check the api url and try again!')
  return res


def get_password_leaks_count(hashes, hash_to_check):
  '''read the response from api data and
     return the number of the count of compromise
  '''
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for hash, count in hashes:
    if hash == hash_to_check:
      return count
  return 0


def pwned_api_check(password):
  '''check if hash password in api data'''
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)


def main(file):
  '''main function that execute the script'''
  with open(file, "r") as args:
    for line in args:
      for password in line.split():
        count = pwned_api_check(password)
        if count:
          print(
            f'{password} was found {count} times... you should probably change your password!'
          )
        else:
          print(f'{password} was NOT found. Carry on!')

  return '-----All Checks Done!-----'


if __name__ == '__main__':
  sys.exit(main(str(sys.argv[1])))
