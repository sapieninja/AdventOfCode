today=$(date +'%-d')
python3 --version
for x in $(seq -f "%02g" 1 "$today") 
do
echo "Day:$x"
echo "___________________________"
time -f %E python3 ./AdventOfCode/Python/$x.py
done