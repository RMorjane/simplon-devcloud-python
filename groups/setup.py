import setuptools

#from setuptools import setup, find_packages
  
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = 'Groups package'
  
setuptools.setup( 
        name ='mygroups', 
        version ='1.0.0', 
        author ='Morjane', 
        author_email ='rhellabmorjane@gmail.com', 
        url ='https://github.com/RMorjane/simplon-devcloud-python/tree/master/groups', 
        description ='application qui gère la répartition des groupes', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        packages = setuptools.find_packages(),
        entry_points ={ 
            'console_scripts': [ 
                'makegroups = mygroups.groups:main',
            ], 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        python_requires='>=3.6'
) 