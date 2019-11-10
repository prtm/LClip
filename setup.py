import setuptools
with open("ReadME.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='lclip',
    version='0.1',
    scripts=['lclip.py'],
    author="Preetam",
    author_email="contact@preetam.dev",
    description="LClip script helps you search clipboard data on your linux favourite browser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prtm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: POSIX :: Linux",
    ],
    install_requires=[
        'pyperclip>=1.7.0',
        'validators>=0.14.0',
    ]
)
