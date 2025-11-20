from semantic_register import SemanticRegister

def execute(op, args, registers, cache, gsf):
    if op == "SEM.MAKE":
        reg = args[0]
        val = float(args[1])
        registers[reg] = SemanticRegister(val, ps=0.01, ws=0.01)

    elif op == "SEM.ADD":
        reg = args[0]
        a = float(args[1])
        b = float(args[2])

        r = registers[reg]
        r.V = a + b
        r.PS += 0.25
        r.WS += 0.05

    elif op == "SEM.WRITE":
        idx = int(args[0].replace("CM[","").replace("]",""))
        reg = args[1]
        cache.write(idx, registers[reg])
