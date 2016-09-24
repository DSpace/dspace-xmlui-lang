# Migration of DSpace XMLUI lang
## About
The aim of this project is to migrate all non-English translations to 
v5.5

##Quick usage
1. Place `messages.xml`, `lang-util.py`, `file-iterator.py` in the _i18n_ 
folder.
2. Issue the command `python3 file-iterator.py` to convert all old xml 
files to the latest version.

###Notes
- Translation strings from the old translation file are migrated over 
by comparing keys.
- If a key in the latest version does not exist in the older version, 
it defaults to English
- `messages.xml` is taken from the master 5.5 release of DSpace.

