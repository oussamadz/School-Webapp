#!/bin/bash
cd $1;
result=${PWD##*/} 
for i in ` ls -p static/$1/images/* | grep -v :`; do
	RS="$(basename -- $i)";
	#echo "------ $RS";
	ss=`find . -type f \( -name "*.html" -o -name "*.css" -o -name "*.scss" -o -name "*.js" -o -name "*.jpg" -o -name "*.png" \)  -exec grep -H $RS {} \; | wc -l`;
	echo -n "$ss : $RS"
	if [ $ss = 0 ]; then
		echo -ne " \t\t--- not used";
	fi
	echo ""
done

echo "current dir: $result"
