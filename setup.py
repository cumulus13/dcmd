from setuptools import setup, find_packages
import __version__
version = __version__.version
setup(
    name = 'dcmd',
    version = version,
    author = 'Hadi Cahyadi LD',
    author_email = 'cumulus13@gmail.com',
    description = ('simple hide, list, show and rechange windows terminal (cmd)'),
    license = 'MIT',
    keywords = "pywin32 terminal win32",
    url = 'https://github.com/cumulus13/dcmd',
    scripts = [],
    py_modules = ['dcmd'],
    packages = find_packages(),
    download_url = 'https://github.com/cumulus13/dcmd/tarball/master',
    install_requires=[
        'psutil',
        'make_colors',
        'pydebugger'
    ],
    # TODO
    #entry_points={
    #    "console_scripts": ["drawille=drawille:__main__"]
    #},
    entry_points = {
         "console_scripts": ["dcmd = dcmd:usage",]
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        'Environment :: Console',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
