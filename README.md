<h1 align="center">nsubdomain-finder</h1>

> Perform dns-bruteforce for enumerating subdomains using nmap tool.


## Installation

> [!IMPORTANT]
>  Ensure you have [nmap](nmap.org) tool installed.

```sh
pip install nsubdomain-finder[cli]
```

## Usage 

<details>

<summary>

`$ nsubfinder --help`
</summary>

```
usage: nsubfinder [-h] [-v] [-t ipv4|ipv6|ipv4v6] [--json] domain

Perform dns-bruteforce for enumerating subdomains using nmap tool

positional arguments:
  domain                Domain name to perform enumeration

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -t ipv4|ipv6|ipv4v6, --type ipv4|ipv6|ipv4v6
                        IP type defaults to ipv6
  --json                Stdout results in json format

```

</details>
