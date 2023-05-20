#!/bin/sh
EXEC_FILE=$1
DIR=$(dirname $EXEC_FILE)
FILE=$(basename $EXEC_FILE .py)
# INPUT=$(cat ${DIR}/${FILE}_input)
# RESULT=$(python $1 <${DIR}/${FILE}_input | tee ${DIR}/${FILE}_output)
python $1 <${DIR}/${FILE}_input | tee ${DIR}/${FILE}_output

# echo 'input>'
# echo $INPUT
# echo 'output>'
# echo $OUTPUT