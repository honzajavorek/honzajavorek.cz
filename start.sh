#!/bin/bash


# Simple BASH script to begin work on project.
# - Sass/Scss compiler
# - opens terminal at project directory with virtualenv activated


PROJECT_DIR=`dirname $0`
CSS_DIR="$PROJECT_DIR/css"


RCFILE=`tempfile`
echo ". ~/.bashrc" >> $RCFILE

VIRTUALENV_RCFILE=`tempfile`
cat $RCFILE >> $VIRTUALENV_RCFILE
echo ". $PROJECT_DIR/env/bin/activate" >> $VIRTUALENV_RCFILE


SERVER_RCFILE=`tempfile`
cat $VIRTUALENV_RCFILE >> $SERVER_RCFILE
echo "cd $PROJECT_DIR/src
until blogofile serve 3838; do
    echo 'Blogofile crashed with exit code $?. Respawning...' >&2
    sleep 5
done
" >> $SERVER_RCFILE

SASS_RCFILE=`tempfile`
cat $RCFILE >> $SASS_RCFILE
echo "sass --style expanded --debug-info --watch $CSS_DIR" >> $SASS_RCFILE

SHELL_RCFILE=`tempfile`
cat $VIRTUALENV_RCFILE >> $SHELL_RCFILE
echo "cd $PROJECT_DIR" >> $SHELL_RCFILE


if which gnome-terminal &> /dev/null; then
    # GNOME Terminal
    exec gnome-terminal\
        --geometry="85x24+850+100"\
        --tab -e "bash --rcfile $SERVER_RCFILE" -t "Server"\
        --tab -e "bash --rcfile $SASS_RCFILE" -t "Sass/Scss"\
        --tab -e "bash --rcfile $SHELL_RCFILE" -t "Shell"

else
    echo "Your terminal is not supported."
fi


rm $RCFILE $VIRTUALENV_RCFILE $SERVER_RCFILE $SHELL_RCFILE

