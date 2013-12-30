from setuptools import setup

setup(
    name='lazyweb',
    version='0.1',
    description='A lightweight jinja template compiler',
    author='Brian McFee',
    author_email='brm2132@columbia.edu',
    url='http://github.com/bmcfee/lazyweb',
    download_url='http://github.com/bmcfee/lazyweb/releases',
    long_description="""\
        Python module for audio and music processing.
    """,
    scripts=['lazyweb.py'],
    classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Multimedia :: Text Processing :: Markup",
    ],
    keywords='web template',
    license='GPL',
    install_requires=[
        'jinja2',
        'ujson',
    ],
    extras_require = {
        'cPickle': 'cPickle'
    }
)
