#!/usr/bin/env bash

GREEN="\033[32m"
NORMAL="\033[0;39m"

# execute docker run command
echo ''
echo ''
echo ''
echo -e "$GREEN### Actual command output ###$NORMAL"
echo ''
echo ''
echo ''
eval $@
COMMAND_EXIT_CODE=$?
echo ''
echo ''
echo ''
echo -e "$GREEN### End actual command output ###$NORMAL"
echo ''
echo ''
echo ''

exit ${COMMAND_EXIT_CODE}