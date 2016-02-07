from setuptools import setup

install_requires = [
    'lxml',
    'requests'
]

tests_require = [
    'nose'
]

setup(name='romspam',
      version='1.0',
      description='Spam bae with sappy messages over social media on V-Day.',
      classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Communications'
      ],
      keywords='valentine valetine\'s day bae sappy love romantic messages social media twitter instagram facebook random generator',
      url='http://github.com/mjmeli',
      author='Michael Meli',
      author_email='mjmeli@ncsu.edu',
      packages=['romspam'],
      entry_points={
        'console_scripts':['romspam=romspam.__main__:main']
      },
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=tests_require,
      install_requires=install_requires
)
