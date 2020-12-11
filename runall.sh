today=$(date +'%-d')
sudo apt install python3
python3 --version
for x in $(seq -f "%02g" 1 "$today") 
do
echo "Day:$x"
python3 ./AdventOfCode/Python/$x.py
done