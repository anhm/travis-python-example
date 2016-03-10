HOME_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "PYTHONPATH=$HOME_PATH/src"
PYTHONPATH=$HOME_PATH/src:$PYTHONPATH
