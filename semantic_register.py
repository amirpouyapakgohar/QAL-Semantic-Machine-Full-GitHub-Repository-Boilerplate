class SemanticRegister:
    def __init__(self, value=0.0, ps=0.0, ws=0.0, c=0.0, m=0.0):
        self.V = value
        self.PS = ps
        self.WS = ws
        self.C = c
        self.M = m

    def __repr__(self):
        return f"(V={self.V:.3f}, PS={self.PS:.4f}, WS={self.WS:.4f}, C={self.C:.4f}, M={self.M:.4f})"
