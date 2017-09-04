from distutils.core import setup
from brewer.version import VERSION

setup(
    name='brewer',
    packages=['brewer'],
    version=VERSION,
    description='A package to control our brew rig',
    author='Luke Sweeney',
    author_email='luke@thesweeneys.org',
    url='https://github.com/llamicron/brewer',
    download_url='https://github.com/llamicron/brewer/archive/0.1.tar.gz',
    keywords=['beer', 'python', 'brewing'],
    classifiers=[],
)
