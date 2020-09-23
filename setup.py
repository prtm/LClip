import setuptools
with open("ReadME.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='lclip',
    version='0.1.3',
    scripts=['lclip'],
    author="Preetam",
    author_email="contact@preetam.dev",
    description="LClip script helps you search clipboard data on your linux favourite browser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prtm/LClip",
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
