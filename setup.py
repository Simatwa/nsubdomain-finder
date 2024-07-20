from setuptools import setup


INSTALL_REQUIRE = []

cli_reqs = ["rich==13.3.4"]


EXTRA_REQUIRE = {
    "cli": cli_reqs,
}

setup(
    name="nsubdomain-finder",
    version="0.0.4",
    license="MIT",
    author="Smartwa",
    maintainer="Smartwa",
    author_email="simatwacaleb@proton.me",
    description="Perform dns-bruteforce for enumerating subdomains using nmap tool",
    packages=["nsubdomain_finder"],
    url="https://github.com/Simatwa/nsubdomain-finder",
    project_urls={
        "Bug Report": "https://github.com/Simatwa/nsubdomain-finder/issues/new",
        "Homepage": "https://github.com/Simatwa/nsubdomain-finder",
        "Source Code": "https://github.com/Simatwa/nsubdomain-finder",
        "Issue Tracker": "https://github.com/Simatwa/nsubdomain-finder/issues",
        "Download": "https://github.com/Simatwa/nsubdomain-finder/releases",
        "Documentation": "https://github.com/Simatwa/nsubdomain-finder/blob/main/README.md",
    },
    entry_points={
        "console_scripts": [
            "nsubfinder = nsubdomain_finder.console:main",
        ],
    },
    install_requires=INSTALL_REQUIRE,
    extras_require=EXTRA_REQUIRE,
    python_requires=">=3.9",
    keywords=[
        "subdomain",
        "subdomain-finder",
        "nsubdomain-finder",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "License :: Free For Home Use",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
