apt install python3
pip install collections more-itertools
today=$(date +'%-d')
for x in $(seq -f "%02g" 1 "$today") 
do
echo "Day:$x"
python3 ./AdventOfCode/Python/$x.py
done