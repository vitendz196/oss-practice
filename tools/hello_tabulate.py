import argparse
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(description="Custom greeting and system info tool")
    parser.add_argument("--name", default="Student", help="User name to greet")
    args = parser.parse_args()

    table_data = [
        ["User", args.name],
        ["Role", "Contributor"],
        ["Course", "Open Source Software"],
        ["Library", "tabulate (v0.10.0)"],
        ["Status", "Ready"]
    ]

    print(f"=== Open Source Workspace: Welcome, {args.name}! ===")
    print(tabulate(table_data, headers=["Attribute", "Details"], tablefmt="grid"))

if __name__ == "__main__":
    main()