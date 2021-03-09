from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="mine_dwarf",
    version='0.1',
    py_modules=['mine_dwarf', 'core', 'file'],
    install_requires=required,
    entry_points= {'console_scripts':
    ['minedwarf=mine_dwarf.mine_dwarf:run_main',]
    }
        
)