echo "[TASK 1] Executing Testcases"
python3 regression.py > reg.txt
echo "[TASK 2] Transform output to html format"
echo "<html><body>" > reg.html
echo "<h1>Regression Automation</h1>" >> reg.html
echo "[TASK 3] Transform using awk"
cat reg.txt | awk -F "|" -f regression.awk >> reg.html
echo "[TASK 4] End of Transform output to html format"
echo "<br/>" >> reg.html
echo "</body></html>" >> reg.html
