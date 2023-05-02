from setuptools import setup, find_packages

setup(
	name='patternanalysis',
	version="1.0.0",
	url='https://github.com/vrijeuniversiteit/patternanalysis.git',
	author='Daniel Müller',
	author_email='d.muller at vu.nl',
	description='Analyzing temporal patterns in timeseries data',
	packages=find_packages(),
	install_requires=['numpy >= 1.24.0', 'tabulate >= 0.9.0'],
	python_requires=">=3.6",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
)
