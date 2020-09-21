from distutils.core import setup

setup(
  name = 'testpypijuhee',
  packages = ['testpypijuhee'],
  version = '0.1',
  license='MIT',
  description = 'test how to upload package on PyPi',
  author = 'Kang Juhee',
  author_email = 'treeinblu@gmail.com',
  url = 'https://github.com/JuheeKang04/testpypijuhee',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['TEST'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: KB KOOKMIN BANK',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)