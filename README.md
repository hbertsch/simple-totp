# Simple `TOTP` Generator
Simple `TOTP` generator that gives you a code based on a key.

`TOTP` an extension of the HMAC-based One-Time Password ([HOTP](https://datatracker.ietf.org/doc/html/rfc4226)). The HOTP algorithm is based on an increasing counter value and a  static symmetric key known only to the token and the validation  service. For TOTP the increasing counter is based on the current time. The secret key is only known to the `generator`(usually a smartphone App) and the `validator`(usually a Web-Service) and can be used to generate or verify a `TOTP`code.

## DISCLAIMER 

This tool doesn't have any security implemented whatsoever. You will need to work with your raw `TOTP` keys, which can be dangerous, since they acre **secrets**.

For this project this should be fine, since en- and decryption of the keys would just add additional code and complexity and is not helpful to understand how the generator is working. 

## How to use

Just hand over the required arguments to the script and enjoy the show:

````shell
# Args:
# -d How many digits your code should have (6 is the default that is used almost everywhere)
# -k Your TOTP key / secret (can be extracted from QR codes)
# -h help

python3 -d 6 -k HIWSCG5ZZFOTLBJUN5RG6U3YKJ3XMY -a sha1
# Example output
>> 823873
````

## Credits

- Thanks to the [oath](https://github.com/bdauvergne/python-oath) project, which was a very good reference
- [RFC6238](https://datatracker.ietf.org/doc/html/rfc6238) 

