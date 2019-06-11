# !/bin/bash
# script should be run from root directory of git repository
# Example call:
# sh ./fasttext_gridsearch_trainer.sh -i data/fasttext/lc/ -o fasttext_models/lc/
# uses hyperparameters found to work best with fasttext_gridsearch_trainer.sh
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
echo ""
echo "Iterating learning rate..."
for i in `seq 0.1 0.1 1`
do
  echo ""
  echo "Training with learning rate = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext supervised \
  -input $inpath/train.txt \
  -output $outpath/quora.lr_$i \
  -lr $i \
  -epoch 4 \
  -wordNgrams 2 \
  -dim 100
  echo "Validating with learning rate = "$i
  /Applications/anaconda3/envs/TM_FS19/bin/fasttext test $outpath/quora.lr_$i.bin $inpath/valid.txt 1
  echo "Removing current models..."
  rm $outpath/quora.lr_$i.*
done
echo ""
echo "Training completed."
