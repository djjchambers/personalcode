try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'Dan Chambers',
    'url': 'URL to get it at',
    'download URL': 'Where to download it',
    'author_email': 'djjchambers@gmail.com',
    'version': '0.1',
    'install requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)