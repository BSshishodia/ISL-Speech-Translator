class ContextMemory:
    def __init__(self):
        self.last_object = None
    
    def update_memory(self, tokens):
        for word in tokens:
            if word not in ["मैं", "तुम", "वह"]:
                self.last_object = word
    
    def resolve_reference(self, tokens):
        if "यह" in tokens or "वह" in tokens:
            tokens = [self.last_object if w in ["यह", "वह"] else w for w in tokens]
        return tokens