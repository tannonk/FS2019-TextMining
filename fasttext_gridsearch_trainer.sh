# !/bin/bash
# script should be run from root directory of git repository
# Example call:
# sh ./fasttext_gridsearch_trainer.sh -i data/fasttext/lc/ -o fasttext_models/lc/
while getopts ":i:o:" opt; do
  case ${opt} in
    i )
      inpath=$OPTARG
      ;;
    o )
      outpath=$OPTARG
      ;;
    \? )
      echo "Usage: cmd [-i] [-o]"
      ;;
    : )
      echo "Invalid option: $OPTARG requires an argument" 1>&2
      ;;
  esac
done
echo ""
echo "Establinging output path..."
mkdir $outpath
echo "Starting mulitple training iterations with $inpath"
echo ""
echo "Training default settings..."
/Applications/anaconda3/envs/TM_FS19/bin/fasttext supervised \
-input $inpath/train.txt \
-output $outpath/quora.default
echo "Validating default settings..."
/Applications/anaconda3/envs/TM_FS19/bin/fasttext test $outpath/quora.default.bin $inpath/valid.txt 1
echo ""
echo "Iterating epochs..."
for i in `seq 1 1 20`
do
  echo ""
  echo "Training with epoch = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext supervised \
  -input $inpath/train.txt \
  -output $outpath/quora.epoch_$i \
  -epoch $i
  echo "Validating with epoch = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext test $outpath/quora.epoch_$i.bin $inpath/valid.txt 1
  echo "Removing current models..."
  rm $outpath/quora.epoch_$i.*
done
echo ""
echo "Iterating ngrams..."
for i in `seq 1 1 5`
do
  echo ""
  echo "Training with word ngrams = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext supervised \
  -input $inpath/train.txt \
  -output $outpath/quora.wordNgrams_$i \
  -wordNgrams $i
  echo "Validating with word ngrams = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext test $outpath/quora.wordNgrams_$i.bin $inpath/valid.txt 1
  echo "Removing current model..."
  rm $outpath/quora.wordNgrams_$i.*
done
echo ""
echo "Iterating dimensions..."
for i in `seq 50 50 500`
do
  echo ""
  echo "Training with dim = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext supervised \
  -input $inpath/train.txt \
  -output $outpath/quora.dim_$i \
  -dim $i
  echo "Validating with dim = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext test $outpath/quora.dim_$i.bin $inpath/valid.txt 1
  echo "Removing current model..."
  rm $outpath/quora.dim_$i.*
done
echo ""
echo "Training completed."

# /Applications/anaconda3/envs/TM_FS19/bin/fasttext predict ....bin
