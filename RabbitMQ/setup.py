from setuptools import setup, find_packages

setup(
    name='RabbitMQ',     
    version='0.1.0',                
    packages=find_packages(),        
    install_requires=[
        'pika',                   
    ],
    description='A simple RabbitMQ wrapper with Producer, Consumer and Connection',
    python_requires='>=3.7',
)
