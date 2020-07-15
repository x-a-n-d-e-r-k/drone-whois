from distutils.core import setup

setup(
    name='drone-whois',
    version='2.0.0',
    author='Tom Steele, XanderK',
    author_email='tom@stacktitan.com, xanderk@notbo.red',
    scripts=['src/drone-whois'],
    url='https://github.com/x-a-n-d-e-r-k/drone-whois',
    license='LICENSE',
    description='IPWhois tool for Lair.',
    install_requires=[
        "pylair >= 2.0.0",
        "ipwhois > 1.0.0",
        "docopt >= 0.6.2",
        "ipaddr==2.1.11"
    ],
)
