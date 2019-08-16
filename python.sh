#!/bin/sh
EXEC_FILE=$1
DIR=$(dirname $EXEC_FILE)
FILE=$(basename $EXEC_FILE .py)
python $1 <${DIR}/${FILE}_input | tee ${DIR}/${FILE}_output
