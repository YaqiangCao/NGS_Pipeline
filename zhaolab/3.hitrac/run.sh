d=`pwd`
echo $d

cd $d/2.tracPre2/ 
sh run.sh

cd $d/3.cLoops2/
python run.py

cd $d/4.tss
python run.py 

rm $d/2.tracPre2/*/*.fastq.gz
rm $d/2.tracPre2/*/*all*
rm $d/2.tracPre2/*/*.bam
