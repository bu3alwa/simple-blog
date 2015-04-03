from setuptools import setup, find_packages

setup(
        name='pyapp',
        version='0.1',
        packages=['pyapp'],
        zip_safe=False,
        include_package_data=True,
        install_requires=[
            'passlib', 
            'MySQL-python', 
            'tornado', 
            'pyyaml', 
            'flask', 
            'pymysql',
            'sqlalchemy', 
            'flask-sqlalchemy']
)
