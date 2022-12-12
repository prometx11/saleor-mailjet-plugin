import setuptools

setuptools.setup(
    name='mailjet',
    version='0.1.00',
    description='Saleor plugin for sending transactional emails with mailjet.',
    author='David Janisch',
    author_email='',
    license='MIT',
    packages=['mailjet'],
    entry_points={
        'saleor.plugins': ['mailjet=mailjet.plugin:MailjetEmailPlugin'],
    },
    # python_requires=">=3.6",
)
