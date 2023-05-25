# Password Checker

The <strong>check_my_pass.py</strong> help check if a password have been compromise before
and count how many times it has been compromise.

# Special Package used
Its uses the request library to request api data from <a href="api.pwnedpasswords.com">PWNEDPASSWORD API</a>
Use the hashlib library to hash password with sha1

The script read the password from a file that its path is added to the command argv.

A simple file is added (password.txt) which can be tasted by running the command:
  - python3 check_my_pass.py passwords.txt
