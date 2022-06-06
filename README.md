# username-generator
A cheap CLI for generating usernames using &lt;adjective>-&lt;noun> format. This was inspired by Docker's [names generator](https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go). See also [my extremely safe, secure, and cutting edge password generator](https://github.com/lcdunne/password-generator).

## Usage
### CLI
```
$ python namegen.py

smoggy-fat
```

Specify the number of usernames to make:
```
$ python namegen.py -n 5

superficial-mind
homely-planet
fuzzy-marriage
floppy-needle
irritable-reflection
```
