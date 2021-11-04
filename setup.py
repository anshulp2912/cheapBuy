from setuptools import setup

setup(name='cheapBuy',
      version='1.0',
      description='cheapBuy Extension provides you ease to buy any product through your favourite website like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites to extension.',
      author='Hardik, Het, Vineet, Saloni, Kalgee',
      author_email='hetpatel0199@gmail.com',
      url='https://github.com/het-patel99/cheapBuy.git',
      packages=['cheapBuy'],
      long_description="""\
            Hands on for the standard github repo files.
            .gitignore
            .travis.yml
            CITATION.md : fill on once you've got your ZENODO DOI going
            CODE-OF-CONDUCT.md
            CONTRIBUTING.md
            LICENSE.md
            README.md
            setup.py
            requirements.txt
            data/
              README.md
            test/
              README.md
            code/
              __init__.py
        """,
      classifiers=[
            "License :: MIT License",
            "Programming Language :: Python",
            "Development Status :: Initial",
            "Intended Audience :: Developers",
            "Topic :: Software Engineering",
        ],
      keywords='python requirements license gitignore',
      license='MIT',
      install_requires=[
            'BeautifulSoup',
            'pytest',
            'Flask',
            'Flask-Cors',
            'webdriver_manager'
        ],
     )
