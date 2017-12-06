# Brewer
A attempt at controlling a homemade homebrewing rig, at home.

See [adaptiman/adaptibrew](http://github.com/adaptiman/adaptibrew) for more details.

## Installation
Note: You probably don't want to install this. For anything to work, you need quite a bit of hardware. If you have the hardware set up correctly, then you already know what you're doing. Otherwise:

```
  $ pip install brewer
```

Or build from source:

```
  $ git clone http://github.com/llamicron/brewer.git
  $ cd brewer
  $ make build
  $ pip install dist/brewer-[VERSION-NUMBER].tar.gz
```

## Docs
See the docs at [ReadTheDocs](http://brewer.readthedocs.io/en/latest/). Unless you like to read raw markdown, in which case you can check out the `docs/` directory.

## Usage
Warning: You should probably be using [weber](http://github.com/llamicron/weber/). It does the same thing as this, but it's a web interface instead of a command line one.

After installation (see above), run `brewer` from a command line. If you cloned this project with git, then run `python brewer.py` in the root directory.

Now you can control your hardware. Try something like this:
```
>> con.hlt(1)
>> con.hlt(0)
```

This should open and close the `hlt` valve (assuming you have a standard setup with an HLT).
