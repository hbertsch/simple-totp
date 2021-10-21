# Simple `totp` Generator
Simple `totp` generator that gives you a code based on a key.

## DISCLAIMER 

this tool doesn't have any security implemented whatsoever. You will need to work with your raw `totp` keys, which can be dangerous, since they acre **secrets**.

For this project this should be fine, since en- and decryption of the keys would just add additional code and complexity and is not helpful to understand how the generator is working. 

## How to use

Just hand over the required arguments to the script and enjoy the show:

````shell
# Args:
# -d How many digits your code should have (6 is the default that is used almost everywhere)
# -k Your TOTP key / secret (can be extracted from QR codes)
# -a Select you algorithm (sha1 is the default)
# -h help

python3 -d 6 -k HIWSCG5ZZFOTLBJUN5RG6U3YKJ3XMY -a sha1
# Example output
>> 823873
````

## Credits

- Thanks to the [oath](https://github.com/bdauvergne/python-oath) project, which was a very good reference
- [RFC6238](https://datatracker.ietf.org/doc/html/rfc6238) 

