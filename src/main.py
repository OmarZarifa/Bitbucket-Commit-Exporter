import argparse
from bitbucket_api import fetch_commits
from doc_writer import write_commits_to_doc

def parse_args():
    parser = argparse.ArgumentParser(
        description="Fetch Bitbucket commits and export them to a Word document."
    )
    parser.add_argument(
        '--user', '-u',
        help="Bitbucket username (will prompt if omitted)",
        default=None
    )
    parser.add_argument(
        '--repo-owner', '-o',
        help="Workspace or user that owns the repo (will prompt if omitted)",
        default=None
    )
    parser.add_argument(
        '--repo-slug', '-r',
        help="The repository slug (will prompt if omitted)",
        default=None
    )
    parser.add_argument(
        '--output', '-f',
        help="Output .docx filename",
        default="commits.docx"
    )
    parser.add_argument(
        '--limit', '-n',
        type=int,
        default=10,
        help="Number of commits to fetch"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Prompt for anything not provided on the CLI
    username   = args.user       or input("Bitbucket username: ")
    repo_owner = args.repo_owner or input("Bitbucket workspace/user (repo owner): ")
    repo_slug  = args.repo_slug  or input("Repository slug: ")
    password   = input("Bitbucket App password: ") 

    # Fetch commits
    commits = fetch_commits(
        username=username,
        app_password=password,
        repo_owner=repo_owner,
        repo_slug=repo_slug,
        limit=args.limit
    )

    # Write to Word doc
    write_commits_to_doc(args.output, commits)

if __name__ == '__main__':
    main()
