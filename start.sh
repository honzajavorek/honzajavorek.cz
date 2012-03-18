#!/bin/bash


# Simple BASH script to begin work on project.
# - Pelican compiler
# - Sass/Scss compiler
# - opens terminal at project directory with virtualenv activated


PROJECT_DIR=`dirname $0`
CSS_DIR="$PROJECT_DIR/theme/static"


RCFILE=`tempfile`
echo ". ~/.bashrc" >> $RCFILE

VIRTUALENV_RCFILE=`tempfile`
cat $RCFILE >> $VIRTUALENV_RCFILE
echo ". $PROJECT_DIR/env/bin/activate" >> $VIRTUALENV_RCFILE


PELICAN_RCFILE=`tempfile`
cat $VIRTUALENV_RCFILE >> $PELICAN_RCFILE
echo "cd $PROJECT_DIR
until pelican -r -s settings.py; do
    echo 'Pelican crashed with exit code $?. Respawning...' >&2
    sleep 5
done
" >> $PELICAN_RCFILE

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
        --tab -e "bash --rcfile $PELICAN_RCFILE" -t "Pelican"\
        --tab -e "bash --rcfile $SASS_RCFILE" -t "Sass/Scss"\
        --tab -e "bash --rcfile $SHELL_RCFILE" -t "Shell"

else
    echo "Your terminal is not supported."
fi


rm $RCFILE $VIRTUALENV_RCFILE $PELICAN_RCFILE $SHELL_RCFILE

