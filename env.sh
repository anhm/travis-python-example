HOME_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $HOME_PATH
PYTHONPATH=$HOME_PATH/src:$PYTHONPATH
echo $PYTHONPATH
