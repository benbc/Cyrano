from setuptools import setup, find_packages

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    ]

setup(name='cyrano',
      version='0.0',
      description='cyrano',
      long_description='',
      classifiers=[],
      author='',
      author_email='',
      url='',
      keywords='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='cyrano',
      install_requires = requires,
      entry_points = """\
      [paste.app_factory]
      main = cyrano:main
      [console_scripts]
      populate_cyrano = cyrano.scripts.populate:main
      """,
      )

