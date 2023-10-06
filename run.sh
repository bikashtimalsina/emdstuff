#!/bin/bash
workdir=`pwd`
for (( i=1; i<=20; i++ )){
dirname=`echo "./Run${i}"`
echo $dirname
mkdir $dirname
cp ./model.xyz $dirname
cp ./nep.txt $dirname
cp ./run.in $dirname
cd $dirname
/kaggle/working/bikash/gpm/src/gpumd < run.in > outputfile
wait $!
cd $workdir
}
