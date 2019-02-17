from setuptools import setup

# Function to open the README file.
def readme():
    with open('README.md') as f:
        return f.read()

setup(name='JSutils',
      version='0.2.1',
      description='Simple to use functions to emulate native functions like setInterval in JavaScript',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 4 - Beta',
        # Define intended audience for package to be developers
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        # Specify the pyhton versions that are supported
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities'
      ],
      keywords='setInterval loop interval',
      url='https://github.com/Jaimeloeuf/JSutils',
      # Link to the Assets hosted on Github
      download_url='https://github.com/Jaimeloeuf/JSutils/archive/v0.2.0.tar.gz',
      author='Jaime Loeuf',
      author_email='jaimeloeuf@gmail.com',
      license='MIT',
      packages=['JSutils'],
      # Do not copy over non-code files when package is installed
      include_package_data=False,
      zip_safe=False)