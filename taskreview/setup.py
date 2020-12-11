import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Taskreview-Package",
    version = "0.1",
    author = "Lara Bertram, Anne Giesen",
    author_email = "lara.bertram@study.hs-duesseldorf.de, anne.giesen@study.hs-duesseldorf.de",
    description = ("Package that includes all modules for task review"),
    license = "BSD",
    packages=setuptools.find_packages(),
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: ...",
    ],
    python_requires='>=3.6'
)
