import argparse

from pytodoist import todoist

with open('token') as f:
    TOKEN = f.read()

def parse_args():
    parser = argparse.ArgumentParser(description="Add task to todoist")
    parser.add_argument('task', nargs='+',
        help="The description of the task to add, without the date")
    parser.add_argument('--due', '-d',
        help="The due date or time of the task.")
    parser.add_argument('--test', '-t', action='store_true',
        help="Test the script and just print the task and date, without adding it.")
    return parser.parse_args()

def main():
    args = parse_args()
    task = ' '.join(args.task)
    if args.test:
        print("Task={}\nDue={}".format(task, args.due))
    else:
        user = todoist.login_with_api_token(TOKEN)
        inbox = user.get_project('Inbox')
        task = inbox.add_task(task, date=args.due)

if __name__ == '__main__':
    main()
