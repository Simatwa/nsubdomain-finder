import argparse
from nsubdomain_finder import Finder, __version__


def error_handler(func):
    def decorator():
        try:
            func()
        except Exception as e:
            print(f"Quitting - {e.args[1] if e.args and len(e.args)>1 else str(e)}")

    return decorator


@error_handler
def main():
    ips = ["ipv4", "ipv6", "ipv4v6"]
    parser = argparse.ArgumentParser(prog="nsubfinder", description=Finder.__doc__)
    parser.add_argument(
        "-v", "--version", action="version", version=f"nsubdomain-finder v{__version__}"
    )
    parser.add_argument("domain", help="Domain name to perform enumeration")
    parser.add_argument(
        "-t",
        "--type",
        choices=ips,
        default="ipv6",
        help="IP type defaults to %(default)s",
        metavar="|".join(ips),
    )
    parser.add_argument(
        "--json", action="store_true", help="Stdout results in json format"
    )
    args = parser.parse_args()
    f = Finder(args.domain)
    results = f.sort_subdomains(f.run(args.type))

    import rich

    if args.json:
        rich.print_json(data=results, indent=4)
    else:
        from rich.table import Table

        table = Table(show_lines=True, title=f"{args.domain} Subdomains")
        table.add_column("No.", justify="center", style="white")
        table.add_column("Subdomains", style="cyan")
        table.add_column(f"IP Addresses ({args.type})", style="yellow")
        for count, subdomain_ips in enumerate(results.items()):
            subdomain, ips = subdomain_ips
            table.add_row(str(count), subdomain, "\n".join(ips))
        rich.print(table)


if __name__ == "__main__":
    main()
