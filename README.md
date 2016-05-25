For this to work there must be a file called `token` in the root directory, which
must contain the API token for todoist.

This is a simple script for adding a task to todoist from the commandline. Once
installed simply call
```
todo This is the task to add -d today
```
which will add a task named "This is the task to add" to the Inbox project with
a due date of today.

Due dates must be specified with the -d/--due flag, not in the message body, but
can use the full language processing abilities of todoist dates. The due date is
optional, and if not specified then one will not be used in todoist either.

There are limitation on the punctuation which can be used, at least ` and ? should
be avoided, and any quote marks must match.

TODO:
 - Test the token reading when installed
 - Get the installation process working better overall
 - Allow the token to be an envrionment variable instead
 - Add a flag for adding a task to a project other than Inbox
 - Get a full list of disallowed punctuation and limitations
