#!/bin/bash

grep -hRvf ./.ignore_emails <repo_path> | grep -Eo '\b+\w+@+\w+\.com+\b'

# Note: if spacial characters can be in the mail address (NO WHITE SPACE CHARACTERS)--> '\b+\S+@+\S+\.com+\b'