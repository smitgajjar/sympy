from sympy.parsing.sym_expr import SymPyExpression

c_src_type = """
'int a = 10;'
'int b = (a!=10)?(a):(0);'

"""
res_type = SymPyExpression(c_src_type, 'c').return_expr()
# res_type8 = SymPyExpression(c_src_type8, 'c').return_expr()

print(res_type)
# print(res_type8)