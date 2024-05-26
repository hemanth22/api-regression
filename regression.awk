BEGIN {
    print "<br/>"
    print "<table border=\"8\" cellpadding=\"3\" style=\"border-collapse: collapse\">"
    print "<tr>"
    print "<th>Test Case</th>"
    print "<th>Test Case details</th>"
    print "<th>Add</th>"
    print "<th>Sub</th>"
    print "<th>Multi</th>"
    print "<th>Divide</th>"
    print "</tr>"
}

NR > 0 {
    print "<tr><td>"$1"</td><td>"$2"</td><td>"$3"</td><td>"$4"</td><td>"$5"</td><td>"$6"</td></tr>"
}

END {
    print "</table>"
    print "<br/>"
}
