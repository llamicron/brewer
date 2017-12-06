# Brewer
Note: If you'd like to contribute, please read the "Contriuting" section down below.

## File structure - Where everything is
Here is the output of `tree .` as of writing this documentation (subject to change):
```
❯ tree .
.
├── brewer
│   ├── controller.py
│   ├── __init__.py
│   ├── omega.py
│   ├── settings.py
│   ├── slack.py
│   ├── str116.py
│   ├── strike_temp_calculator.py
│   └── version.py
├── brewer.py
├── dist
│   └── brewer-0.2.4.tar.gz
├── docs
│   └── DOC_FILES_HERE.md
├── __init__.py
├── Makefile
├── MANIFEST
├── MANIFEST.in
├── README
├── requirements.txt
├── setup.cfg
├── setup.py
└── tests
    ├── __init__.py
    ├── test_controller.py
    ├── test_omega.py
    ├── test_settings.py
    ├── test_slack.py
    └── test_strike_temp_calculator.py

4 directories, 27 files

brewer git/master*
❯
```

Source code is in the `brewer/` directory, tests in the `tests/` directory, distributions in the `dist/` directory, docs in the `docs` directory. Pretty simple. There are also some loose files in the projet root. These are:
```
.
├── brewer.py
├── __init__.py
├── Makefile
├── MANIFEST
├── MANIFEST.in
├── README
├── requirements.txt
├── setup.cfg
└── setup.py
```

`brewer.py` is the entry point for the command line interface. There are some problems with it, so I tend not to use it until I get around to fixing it. It basically starts a python REPL with all the code imported.

`Makefile`: This one is pretty self explainatory. It has directives like `install`, `build`, `upload`, `test`, etc. Check it out, it's really simple.

`setup.py` is used for python packaging service. It contains details about brewer. If you add something and it's not getting packaged properly, or there are missing depenedencies, you may want to start there.

## Classes
See the [table of contents for classes](classes/index.md)

## Contributing
If you'd like to contribute, there are a few requirements:
1. You (loosely) follow PEP 8. I don't care if it's down to the letter, hell I don't follow it all the time, but I don't want a bowl of speghetti to get submitted as a PR.
2. You write tests. If you use `make test` to run tests, it will use pytest-cov for code coverage. Make sure all your code is covered. Try to break your code and still make your tests pass. If that happens, re-write your tests.
3. You write documentation. Not comments, but docs. If you add a class, add a new `.md` file in the `docs/classes/` dir. Write about it's properties and methods so that I know what the hell I'm looking at. Write why that class is necessary and what it does and how I can use it.

PR won't be accepted if they don't have docs and tests.
