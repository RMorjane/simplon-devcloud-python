import setuptools

#from setuptools import setup, find_packages
  
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = 'Pendu package'
  
setuptools.setup( 
        name ='mypendu', 
        version ='1.0.0', 
        author ='Morjane', 
        author_email ='rhellabmorjane@gmail.com', 
        url ='https://github.com/RMorjane/simplon-devcloud-python/tree/master/pendu', 
        description ='jeu du pendu', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        packages = setuptools.find_packages(),
        entry_points ={ 
            'console_scripts': [ 
                'pendu = mypendu.pendu:main',
            ], 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        python_requires='>=3.6'
) 