def global_semantic_field(registers):
    total = 0.0
    for reg in registers.values():
        total += reg.C * (reg.PS - reg.WS)
    return total
