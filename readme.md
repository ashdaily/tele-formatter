### TeleFormatter for Japanese Phone Numbers

This teleformatter formats japanese phone numbers by looking at their area code prefix.
This is how it works:
- You enter the phone number with area code
- Script looks for a match inside `data/area_codes.txt` file and find the longest matching area code prefix
- Depending on the area code prefix length, it returns a formatted phone number as below:
```
# convert 2 digit prefixes in the format of XX-XXXX-XXXX
> python3 main.py -n 0312345678
03-1234-5678

# convert 3 digit prefixes in the format of XXX-XXX-XXXX
> python3 main.py -n 0300000000
03-0000-0000

# convert 4 digit prefixes in the format of XXXX-XX-XXXX
> python3 main.py -n 0429991111
042-999-1111

# convert 5 digit prefixes in the format of XXXXX-X-XXXX
> python3 main.py -n 0428991111
0428-99-1111

> python3 main.py -n 0126700000
01267-0-0000

# also handles zenkaku characters
03-0000-0000
>  python3 main.py -n ０３−００００−００００
```

### Known issues:
- Doesn't handle cell phone numbers


