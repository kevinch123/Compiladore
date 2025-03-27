from MiGramaticaVisitor import MiGramaticaVisitor

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}

    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.variables

    def visitAssign(self, ctx):
        var = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var] = value
        print(f"📝 {var} = {value}")
        return value

    def visitForLoop(self, ctx):
        var = ctx.inicializacion().ID().getText()
        self.variables[var] = self.visit(ctx.inicializacion().expresion())
        
        while self.visit(ctx.condicion()):
            for sentencia in ctx.sentencia():
                self.visit(sentencia)  
            
            update_var = ctx.actualizacion().ID().getText()
            new_value = self.visit(ctx.actualizacion().expresion())
            self.variables[update_var] = new_value
        
        print("🔄 Finalizó la ejecución del bucle FOR")

    def visitCondicion(self, ctx):
        var = ctx.ID().getText()
        value = self.variables.get(var, 0)
        cmp_value = int(ctx.INT().getText())
        op = ctx.op.text
        
        if op == '>':
            return value > cmp_value
        elif op == '<':
            return value < cmp_value
        elif op == '==':
            return value == cmp_value
        elif op == '!=':
            return value != cmp_value
        return False

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        return left + right if ctx.op.text == '+' else left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        return left * right if ctx.op.text == '*' else left / right

    def visitInt(self, ctx):
        return int(ctx.getText())

    def visitVariable(self, ctx):

        var = ctx.getText()
        if var not in self.variables:
            print(f"⚠️ Variable '{var}' no está inicializada. Se asume 0.")
        return self.variables.get(var, 0)