#!/bin/bash


# Simple BASH script to begin work on project.
# - Pelican compiler
# - Sass/Scss compiler
# - opens terminal at project directory with virtualenv activated


# Define paths to affected directories
PROJECT_DIR=`dirname $0`
CSS_DIR="$PROJECT_DIR/theme/static/css"


# Prepare RC file boilerplate
RCFILE=`tempfile`
echo ". ~/.bashrc" >> $RCFILE

# RC file to activate virtualenv
VIRTUALENV_RCFILE=`tempfile`
cat $RCFILE >> $VIRTUALENV_RCFILE
echo ". $PROJECT_DIR/env/bin/activate" >> $VIRTUALENV_RCFILE

# Pelican RC file to watch changes and automatically recompile
PELICAN_RCFILE=`tempfile`
cat $VIRTUALENV_RCFILE >> $PELICAN_RCFILE
echo "cd $PROJECT_DIR
echo '>>> Pelican is watching for changes. Press Ctrl-C to stop.'
until pelican -r -D -s settings.py; do
    echo 'Pelican crashed. Respawning...' >&2
    sleep 2
done
" >> $PELICAN_RCFILE

# SASS RC file to watch changes and automatically recompile
SASS_RCFILE=`tempfile`
cat $RCFILE >> $SASS_RCFILE
echo "sass --style expanded --debug-info --watch $CSS_DIR" >> $SASS_RCFILE

# Shell RC file, only activates virtualenv and changes directory
# to the project root
SHELL_RCFILE=`tempfile`
cat $VIRTUALENV_RCFILE >> $SHELL_RCFILE
echo "cd $PROJECT_DIR" >> $SHELL_RCFILE


# Launch terminal with tabs, each dedicated to one of the
# tools prepared above
if which gnome-terminal &> /dev/null; then
    # GNOME Terminal
    exec gnome-terminal\
        --geometry="85x24+850+100"\
        --tab -e "bash --rcfile $PELICAN_RCFILE" -t "Pelican"\
        --tab -e "bash --rcfile $SASS_RCFILE" -t "Sass/Scss"\
        --tab -e "bash --rcfile $SHELL_RCFILE" -t "Shell"

elif which xfce4-terminal &> /dev/null; then
    # XFCE Terminal
    exec xfce4-terminal\
        --geometry="85x24+850+100"\
        -e "bash --rcfile $PELICAN_RCFILE" -T "Pelican"\
        --tab -e "bash --rcfile $SASS_RCFILE" -T "Sass/Scss"\
        --tab -e "bash --rcfile $SHELL_RCFILE" -T "Shell"

else
    # I didn't need any other graphic terminal yet.
    echo "Your terminal is not supported."
fi


# Cleanup all temporary RC files.
rm $RCFILE $VIRTUALENV_RCFILE $PELICAN_RCFILE $SASS_RCFILE $SHELL_RCFILE

