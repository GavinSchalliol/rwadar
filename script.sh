#!/bin/bash
source config
touch found.txt

function parse {
  python parse.py $1
}

while [ $ITER -le $LIMIT ]
  do
    # Get web page
    echo "curl -s http://$RWSITE/$ITER.html > pages/$ITER.html" | bash
    exc=$?
    if [[ $exc != 0 ]]
      then echo "Lookup failed, You may be missing the \$RWSITE environment variable. \nExiting..."
      exit 127; fi 

    # log page
    echo "GET page $ITER"
  
    # check page for matching string
    cat "pages/$ITER.html" | grep -qi "refugees welcome" 
    
    # did we find something? let's check the exit code of our  grep  command.
    exc=$?
    
    # if not, delete the saved page
    if [[ $exc != 0 ]]
      then rm "pages/$ITER".html 2&>/dev/null; fi
    
    # if yes, log it
    if [[ $exc = 0 ]]
      then echo "$ITER" >> found.txt; parse pages/$ITER.html; fi
    
  # increment the iterator so we can check the next page
  ITER=$(( ITER+INCR ))

done
