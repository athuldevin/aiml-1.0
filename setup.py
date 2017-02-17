# Command to build:
from distutils.core import setup

setup(name="aiml",
    version="1.0",
    author="Athuldevin",
    author_email="athuldevin@gmail.com",
    maintainer="athuldevin",
    maintainer_email="athuldevin@gmail.com",
    
    description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
    long_description="""PyAIML implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.""",
    url="http://pyaiml.sourceforge.net/",
    platforms=["any"],
    classifiers=["Development Status :: 3 - Alpha",
                 "Environment :: Console",
                 "Intended Audience :: Developers",
                 "Programming Language :: Python",
                 "Operating System :: OS Independent",
                 "Topic :: Communications :: Chat",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence"
                 ],
      
    packages=["aiml"],
    package_dir={'aiml': 'aiml'},
    package_data={'aiml': ['files/aiml/*.aiml',
                           'files/substitutions/*.substitution',
                           'files/system/*.properties',
                           '*.aiml',
                           '*.xml']},
)
