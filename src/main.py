import sys, os; sys.path.append(os.path.join(os.path.dirname(__file__), '..')); import package as ps

ps.fn("main", """

    let("op", iln("Operator: ")) // Operator, +, -, *, /.
    let("first", iln("first : ")) // First number
    let("sec", iln("second : ")) //  Second number
//  ----
    let("result", math("{first} {op} {sec}")) // Does the math
    pln("output:*n{result}*nend") // Outputs the result
    

""")
