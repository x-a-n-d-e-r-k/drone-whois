from distutils.core import setup

setup(
    name='drone-whois',
    version='1.0.0',
    author='Tom Steele',
    author_email='tom@stacktitan.com',
    scripts=['bin/drone-whois'],
    url='https://github.com/lair-framework/drone-whois',
    license='LICENSE',
    description='IPWhois tool for Lair.',
    install_requires=[
        "pylair >= 0.2",
        "ipwhois >= 0.10.2",
        "docopt >= 0.6.2",
        "netaddr >= 0.7.15"
    ],
)
