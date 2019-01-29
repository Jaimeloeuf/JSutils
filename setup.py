from setuptools import setup

# Function to open the README file.
def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='JSutils',
      version='0.2',
      description='Simple to use looping mechanism to emulate the setInterval function in JavaScript',
	  long_description=readme(),
      classifiers=[
        'Development Status :: 4 - Beta',
		'Environment :: Console',
        'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
		'Topic :: Utilities'
      ],
	  keywords='setInterval loop interval',
      url='http://github.com/jaimeloeuf',
      author='Jaime Loeuf',
      author_email='jaimeloeuf@gmail.com',
      license='MIT',
      packages=['JSutils'],
	  include_package_data=True,
      zip_safe=False)