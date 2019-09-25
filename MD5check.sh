#!/bin/bash
# Usage：bash MD5check.sh SAMPLElist.file

echo "MD5 check" > MD5-check.log
for i in `cat $1`;do
cd ${i}
md5sum -c ./MD5_${i}.txt >> ../MD5-check.log
cd ../
done

