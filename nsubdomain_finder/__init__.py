import re
import subprocess
from typing import Literal
from importlib import metadata

try:
    __version__ = metadata.version("nsubdomain-finder")
except metadata.PackageNotFoundError:
    __version__ = "1.0.0"

__repo__ = "https://github.com/Simatwa/nsubdomain-finder"


class Util:

    @staticmethod
    def run_command(command: str) -> subprocess.CompletedProcess:
        """Run command again system and capture output

        Args:
            command (str): command to be run

        Returns:
            subprocess.CompletedProcess: Captured process.
        """
        # Run the command and capture the output
        return subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )


class NmapNotFoundError(Exception):
    """Raised when nmap tool cannot be found"""

    pass


class ZeroSubdomainFoundError(Exception):
    """Enumeration completed with zero finds"""

    pass


class Finder:
    """Perform dns-bruteforce for enumerating subdomains using nmap tool"""

    def __init__(self, domain: str):
        """Constructor

        Args:
            domain (str): The domain to perform the subdomain enumeration
        """
        try:
            self.nmap_version = Util.run_command("nmap --version").stdout
        except subprocess.SubprocessError as e:
            raise "Failed to detect nmap tool in your system." from e

        self.domain = domain

        self._patterns = {
            "ipv4v6": r".\s{5}([\W\w][^\s]+)\s-\s(.+)",
            "ipv4": r".\s{5}([\W\w][^\s]+)\s-\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",
            "ipv6": r".\s{5}([\W\w][^\s]+)\s-\s(\w{1,4}:\w{1,4}.*)",
        }

    def run(
        self, ip_type: Literal["ipv4", "ipv6", "ipv4v6"] = "ipv4v6"
    ) -> list[tuple[str]]:
        """Enumerate subdomains

        Args:
            ip_type (Literal["ipv4", "ipv6", "ipv4v6"], optional): . Defaults to "ipv4v6".

        Returns:
            list[tuple[str]]: [(subdomain, IP)]
        """
        subdomains: list[tuple[str]] = re.findall(
            self._patterns[ip_type],
            Util.run_command(
                f"nmap {self.domain} -p 80,443 --script dns-brute.nse"
            ).stdout,
        )
        if subdomains:
            return subdomains

        raise ZeroSubdomainFoundError(
            "Subdomain enumeration completed without any find."
        )

    def sort_subdomains(self, findings: list[tuple[str]]) -> dict[str, list[str]]:
        """Maps IP addresses resolving to one adress to that particula adress

        Args:
            findings (list[tuple[str]]): Subdomain scan result.

        Returns:
            dict[str, list[str]]: {subdomain_name : [IP addresses]}
        """
        subdomain_map = {}
        for subdomain, ip in findings:
            if subdomain in subdomain_map:
                subdomain_map[subdomain].append(ip)
            else:
                subdomain_map[subdomain] = [ip]
        return subdomain_map
