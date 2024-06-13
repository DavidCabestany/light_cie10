from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cie10-codes-extraction-tool',
    version='0.1.0',
    author='David Cabestany, Paula Ramos, Cristina Mondria, Vicent Cano',
    author_email='david.cabestanymanen@cognizant.com',  # Replace with your email
    description='A tool to extract ICD-10 (CIE-10) codes from PDF documents using Vision model and GPT-4 Omnium.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DavidCabestany-at-cognizant/cie10_tool/',  
    packages=find_packages(),
    install_requires=[
        'gradio>=4.31.5',
        'openai>=1.31.1',
        'pillow>=10.3.0',
        'pytesseract>=0.3.10',
        'pymupdf>=1.24.4',
        'python-dotenv>=1.0.1',
        'pandas>=2.1.4',
        'langchain>=0.2.1',
        'langchain_openai>=0.1.8',
        'langchain_community>=0.2.1',
        'requests>=2.31.0',
        'faiss-gpu>=1.7.2',
        'uvicorn>=0.29.0',
        'fastapi>=0.110.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)
