today=$(date +'%-d')
python3 --version
for x in $(seq -f "%02g" 1 "$today") 
do
echo "Day:$x"
time -f %E python3 ./AdventOfCode/Python/$x.py
echo "___________________________"
done