from setuptools import find_packages, setup

setup(
    name="screenread",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="Have your Windows speak text that's on the screen just like MAC",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['say = screenread:main', ],
    },
    install_requires=["winsay"],

)
