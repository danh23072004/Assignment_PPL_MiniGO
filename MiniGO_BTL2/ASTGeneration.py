# 2210458
from numbers import Number
from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from functools import reduce
from typing import List, Tuple

class ASTGeneration(MiniGoVisitor):
    # program: ((declared))+ EOF;
    def visitProgram(self, ctx: MiniGoParser.ProgramContext):
        list_declared = []
        for declared in ctx.declared():
            list_declared += [self.visit(declared)]
        return Program(list_declared)

    # number: DECINT_LIT | OCTINT_LIT | HEXINT_LIT | BININT_LIT | FLOAT_LIT;
    def visitNumber(self, ctx:MiniGoParser.NumberContext):
        if ctx.DECINT_LIT():
            return IntLiteral(ctx.DECINT_LIT().getText())
        elif ctx.BININT_LIT():
            return IntLiteral(ctx.BININT_LIT().getText())
        elif ctx.OCTINT_LIT():
            return IntLiteral(ctx.OCTINT_LIT().getText())
        elif ctx.HEXINT_LIT():
            return IntLiteral(ctx.HEXINT_LIT().getText())
        elif ctx.FLOAT_LIT():
            return FloatLiteral(ctx.FLOAT_LIT().getText())

    # literal: number | STRING_LIT | TRUE | FALSE | NIL | array_literal | struct_literal;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.number():
            return self.visit(ctx.number())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())

    # grouped_expression: LPAREN expression1 RPAREN;
    def visitGrouped_expression(self, ctx:MiniGoParser.Grouped_expressionContext):
        return self.visit(ctx.expression1())

    # expression1: expression1 OR expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        return BinaryOp(ctx.OR().getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))

    # expression2: expression2 AND expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        return BinaryOp(ctx.AND().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))

    # expression3: expression3 (EQUAL | NOT_EQUAL | LESS | LESS_OR_EQUAL | GREATER | GREATER_OR_EQUAL) expression4 | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        if ctx.EQUAL():
            return BinaryOp(ctx.EQUAL().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.NOT_EQUAL():
            return BinaryOp(ctx.NOT_EQUAL().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.LESS():
            return BinaryOp(ctx.LESS().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.LESS_OR_EQUAL():
            return BinaryOp(ctx.LESS_OR_EQUAL().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        elif ctx.GREATER():
            return BinaryOp(ctx.GREATER().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        return BinaryOp(ctx.GREATER_OR_EQUAL().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))

    # expression4: expression4 (ADD | SUB) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
        return BinaryOp(ctx.SUB().getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))

    # expression5: expression5 (MUL | DIV | MOD) expression6 | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.expression5()), self.visit(ctx.expression6()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.expression5()), self.visit(ctx.expression6()))
        return BinaryOp(ctx.MOD().getText(), self.visit(ctx.expression5()), self.visit(ctx.expression6()))

    # expression6: (NOT | SUB) expression6 | expression7;
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expression6()))
        return UnaryOp(ctx.SUB().getText(), self.visit(ctx.expression6()))

    # expression7: expression7 LSQUAREBRACK expression1 RSQUAREBRACK | expression7 DOT ID | expression7 DOT ID LPAREN expression_list RPAREN | ID LPAREN expression_list RPAREN | final_expression;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.LSQUAREBRACK():
            expression7 = self.visit(ctx.expression7())
            if isinstance(expression7, ArrayCell):
                return ArrayCell(expression7.arr, expression7.idx + [self.visit(ctx.expression1())])
            else:
                return ArrayCell(expression7, [self.visit(ctx.expression1())])
        elif ctx.DOT() and ctx.ID() and ctx.expression_list():
            return MethCall(self.visit(ctx.expression7()), ctx.ID().getText(), self.visit(ctx.expression_list()))
        elif ctx.DOT() and ctx.ID():
            return FieldAccess(self.visit(ctx.expression7()), ctx.ID().getText())
        elif ctx.LPAREN():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.expression_list()))
        return self.visit(ctx.final_expression())

    # final_expression: literal | ID | grouped_expression;
    def visitFinal_expression(self, ctx:MiniGoParser.Final_expressionContext):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.grouped_expression():
            return self.visit(ctx.grouped_expression())

    # expression_list: expression_part | ;
    def visitExpression_list(self, ctx:MiniGoParser.Expression_listContext):
        if ctx.expression_part():
            return self.visit(ctx.expression_part())
        return []

    # expression_part: expression1 COMMA expression_part | expression1;
    def visitExpression_part(self, ctx:MiniGoParser.Expression_partContext):
        if ctx.expression_part():
            return [self.visit(ctx.expression1())] + self.visit(ctx.expression_part())
        return [self.visit(ctx.expression1())]

    # literal_inside_array: ID | struct_literal | STRING_LIT | TRUE | FALSE | NIL | number;
    def visitLiteral_inside_array(self, ctx:MiniGoParser.Literal_inside_arrayContext):
        if ctx.ID():
            return ctx.ID().getText()
        elif ctx.struct_literal():
            return self.visit(ctx.struct_literal())
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.number():
            return self.visit(ctx.number())

    # list_literal: literal_inside_array COMMA list_literal | literal_inside_array;
    def visitList_literal(self, ctx:MiniGoParser.List_literalContext):
        if ctx.list_literal():
            return [self.visit(ctx.literal_inside_array())] + self.visit(ctx.list_literal())
        return [self.visit(ctx.literal_inside_array())]

    # dimension_part: LSQUAREBRACK (DECINT_LIT | ID) RSQUAREBRACK;
    def visitDimension_part(self, ctx:MiniGoParser.Dimension_partContext):
        if ctx.DECINT_LIT():
            return IntLiteral(int(ctx.DECINT_LIT().getText()))
        return Id(ctx.ID().getText())

    # dimension_list: dimension_part dimension_list | dimension_part;
    def visitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        if ctx.dimension_list():
            return [self.visit(ctx.dimension_part())] + self.visit(ctx.dimension_list())
        return [self.visit(ctx.dimension_part())]

    # nested_array_element_list: list_literal | nested_array_element_list COMMA nested_array_element_list | LBRACEBRACK nested_array_element_list RBRACEBRACK COMMA nested_array_element_list | LBRACEBRACK nested_array_element_list RBRACEBRACK;
    def visitNested_array_element_list(self, ctx:MiniGoParser.Nested_array_element_listContext):
        if ctx.LBRACEBRACK() and ctx.nested_array_element_list(0) and ctx.nested_array_element_list(1):
            return [self.visit(ctx.nested_array_element_list(0))] + self.visit(ctx.nested_array_element_list(1))
        elif ctx.LBRACEBRACK() and ctx.nested_array_element_list():
            return [self.visit(ctx.nested_array_element_list(0))]
        elif ctx.list_literal():
            return self.visit(ctx.list_literal())
        elif ctx.nested_array_element_list(0) and ctx.nested_array_element_list(1):
            return self.visit(ctx.nested_array_element_list(0)) + self.visit(ctx.nested_array_element_list(1))

    # list_nested_array_element_list: nested_array_element_list;
    def visitList_nested_array_element_list(self, ctx:MiniGoParser.List_nested_array_element_listContext):
        return self.visit(ctx.nested_array_element_list())

    # array_element_list: LBRACEBRACK list_nested_array_element_list RBRACEBRACK;
    def visitArray_element_list(self, ctx:MiniGoParser.Array_element_listContext):
        return self.visit(ctx.list_nested_array_element_list())

    # array_literal: dimension_list (INT | FLOAT | STRING | BOOLEAN | ID) array_element_list;
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        dimension_list = self.visit(ctx.dimension_list())
        element_type = None
        if ctx.INT():
            element_type = IntType()
        elif ctx.FLOAT():
            element_type = FloatType()
        elif ctx.STRING():
            element_type = StringType()
        elif ctx.BOOLEAN():
            element_type = BoolType()
        elif ctx.ID():
            element_type = Id(ctx.ID().getText())
        array_element_list = self.visit(ctx.array_element_list())
        return ArrayLiteral(dimension_list, element_type, array_element_list)

    # field_element: ID COLON expression1 COMMA field_element | ID COLON expression1;
    def visitField_element(self, ctx:MiniGoParser.Field_elementContext):
        if ctx.field_element():
            return [(ctx.ID().getText(), self.visit(ctx.expression1()))] + self.visit(ctx.field_element())
        return [(ctx.ID().getText(), self.visit(ctx.expression1()))]

    # field_list: field_element | ;
    def visitField_list(self, ctx:MiniGoParser.Field_listContext):
        if ctx.field_element():
            return self.visit(ctx.field_element())
        return []

    # struct_literal: ID LBRACEBRACK field_list RBRACEBRACK;
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        field_list = self.visit(ctx.field_list())
        return StructLiteral(ctx.ID().getText(), field_list)

    # end_statement: SEMICOLON | NEW_LINE;
    def visitEnd_statement(self, ctx:MiniGoParser.End_statementContext):
        return None

    # declared: (const_declared_statement | variable_declared_statement | function_declared_statement | method_declared_statement | struct_declared_statement | interface_declared_statement) end_statement;
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        if ctx.const_declared_statement():
            return self.visit(ctx.const_declared_statement())
        elif ctx.variable_declared_statement():
            return self.visit(ctx.variable_declared_statement())
        elif ctx.function_declared_statement():
            return self.visit(ctx.function_declared_statement())
        elif ctx.method_declared_statement():
            return self.visit(ctx.method_declared_statement())
        elif ctx.struct_declared_statement():
            return self.visit(ctx.struct_declared_statement())
        elif ctx.interface_declared_statement():
            return self.visit(ctx.interface_declared_statement())

    # statement: (const_declared_statement | variable_declared_statement | assignment_statement | for_statement | return_statement | if_statement | break_statement | continue_statement | call_statement) end_statement;
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        if ctx.const_declared_statement():
            return self.visit(ctx.const_declared_statement())
        elif ctx.variable_declared_statement():
            return self.visit(ctx.variable_declared_statement())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.call_statement():
            return self.visit(ctx.call_statement())

    # statement_list: statement statement_list | ;
    def visitStatement_list(self, ctx:MiniGoParser.Statement_listContext):
        if ctx.statement():
            return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())
        return []

    # const_declared_statement: CONST ID INIT expression1;
    def visitConst_declared_statement(self, ctx:MiniGoParser.Const_declared_statementContext):
        expression = self.visit(ctx.expression1())
        return ConstDecl(ctx.ID().getText(), None, expression)

    # array_type: dimension_list required_type;
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimension_list()), self.visit(ctx.required_type()))

    # required_type: INT | FLOAT | STRING | BOOLEAN | ID | array_type;
    def visitRequired_type(self, ctx:MiniGoParser.Required_typeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_type():
            return self.visit(ctx.array_type())

    # optional_type: required_type | ;
    def visitOptional_type(self, ctx:MiniGoParser.Optional_typeContext):
        if ctx.required_type():
            return self.visit(ctx.required_type())
        return VoidType()

    # required_initial_expression: INIT expression1;
    def visitRequired_initial_expression(self, ctx:MiniGoParser.Required_initial_expressionContext):
        return self.visit(ctx.expression1())

    # optional_initial_expression: required_initial_expression | ;
    def visitOptional_initial_expression(self, ctx:MiniGoParser.Optional_initial_expressionContext):
        if ctx.required_initial_expression():
            return self.visit(ctx.required_initial_expression())
        return None

    # variable_declared_statement: VAR ID required_type optional_initial_expression | VAR ID optional_type required_initial_expression;
    def visitVariable_declared_statement(self, ctx:MiniGoParser.Variable_declared_statementContext):
        if ctx.required_type():
            return VarDecl(ctx.ID().getText(), self.visit(ctx.required_type()), self.visit(ctx.optional_initial_expression()))
        optional_type = self.visit(ctx.optional_type())
        if isinstance(optional_type, VoidType):
            return VarDecl(ctx.ID().getText(), None, self.visit(ctx.required_initial_expression()))
        else:
            return VarDecl(ctx.ID().getText(), optional_type, self.visit(ctx.required_initial_expression()))

    # optional_parameter_list: separated_parameter_list | grouped_parameter_list | ;
    def visitOptional_parameter_list(self, ctx:MiniGoParser.Optional_parameter_listContext):
        list_param = []
        param_decl_list = []
        if ctx.separated_parameter_list():
            list_param = self.visit(ctx.separated_parameter_list())
            for param in list_param:
                param_decl_list.append(ParamDecl(param[0], param[1]))
        elif ctx.grouped_parameter_list():
            list_param = self.visit(ctx.grouped_parameter_list())
            for group in list_param:
                for param in group[0]:
                    param_decl_list.append(ParamDecl(param, group[1]))
        return param_decl_list

    # separated_parameter_list: ID required_type COMMA separated_parameter_list | ID required_type;
    def visitSeparated_parameter_list(self, ctx:MiniGoParser.Separated_parameter_listContext):
        if ctx.separated_parameter_list():
            return [(ctx.ID().getText(), self.visit(ctx.required_type()))] + self.visit(ctx.separated_parameter_list())
        return [(ctx.ID().getText(), self.visit(ctx.required_type()))]

    # grouped_parameter_list: variable_list required_type COMMA grouped_parameter_list | variable_list required_type;
    def visitGrouped_parameter_list(self, ctx:MiniGoParser.Grouped_parameter_listContext):
        list_param = [(self.visit(ctx.variable_list()), self.visit(ctx.required_type()))]
        if ctx.COMMA():
            return list_param + self.visit(ctx.grouped_parameter_list())
        return list_param

    # variable_list: ID COMMA variable_list | ID;
    def visitVariable_list(self, ctx:MiniGoParser.Variable_listContext):
        if ctx.variable_list():
            return [ctx.ID().getText()] + self.visit(ctx.variable_list())
        return [ctx.ID().getText()]

    # return_statement: RETURN expression1 | RETURN;
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        if ctx.expression1():
            return Return(self.visit(ctx.expression1()))
        return Return(None)

    # break_statement: BREAK;
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return Break()

    # continue_statement: CONTINUE;
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return Continue()

    # lhs: lhs DOT ID | lhs LSQUAREBRACK expression1 RSQUAREBRACK | ID;
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        if ctx.ID() and not ctx.DOT() and not ctx.LSQUAREBRACK():
            return Id(ctx.ID().getText())
        elif ctx.DOT():
            return FieldAccess(self.visit(ctx.lhs()), ctx.ID().getText())
        elif ctx.LSQUAREBRACK():
            lhs = self.visit(ctx.lhs())
            if isinstance(lhs, ArrayCell):
                return ArrayCell(lhs.arr, lhs.idx + [self.visit(ctx.expression1())])
            else:
                return ArrayCell(lhs, [self.visit(ctx.expression1())])

    # assignment_statement: lhs assign_operator expression1;
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        lhs = self.visit(ctx.lhs())
        op = ctx.assign_operator().getText()
        rhs = self.visit(ctx.expression1())
        if op == ':=':
            return Assign(lhs, rhs)
        elif op == '+=':
            return Assign(lhs, BinaryOp('+', lhs, rhs))
        elif op == '-=':
            return Assign(lhs, BinaryOp('-', lhs, rhs))
        elif op == '*=':
            return Assign(lhs, BinaryOp('*', lhs, rhs))
        elif op == '/=':
            return Assign(lhs, BinaryOp('/', lhs, rhs))
        elif op == '%=':
            return Assign(lhs, BinaryOp('%', lhs, rhs))

    # if_statement: IF LPAREN expression1 RPAREN LBRACEBRACK statement_list RBRACEBRACK else_if_statement_list else_statement;
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        expr = self.visit(ctx.expression1())
        thenStmt = Block(self.visit(ctx.statement_list()))
        else_if_list = self.visitElse_if_statement_list(ctx.else_if_statement_list())
        final_else = self.visitElse_statement(ctx.else_statement())
        current = final_else
        for else_if_expr, else_if_thenStmt in reversed(else_if_list):
            current = If(else_if_expr, else_if_thenStmt, current)
        return If(expr, thenStmt, current)

    # if_in_else_if_statement: IF LPAREN expression1 RPAREN LBRACEBRACK statement_list RBRACEBRACK;
    def visitIf_in_else_if_statement(self, ctx:MiniGoParser.If_in_else_if_statementContext):
        expr = self.visit(ctx.expression1())
        thenStmt = Block(self.visit(ctx.statement_list()))
        return (expr, thenStmt)

    # else_if_statement_list: ELSE if_in_else_if_statement else_if_statement_list | ;
    def visitElse_if_statement_list(self, ctx:MiniGoParser.Else_if_statement_listContext):
        if not ctx or ctx.getChildCount() == 0:
            return []
        else:
            else_if = self.visitIf_in_else_if_statement(ctx.if_in_else_if_statement())
            rest = self.visitElse_if_statement_list(ctx.else_if_statement_list())
            return [else_if] + rest

    # else_statement: ELSE LBRACEBRACK statement_list RBRACEBRACK | ;
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        if ctx.ELSE():
            return Block(self.visit(ctx.statement_list()))
        return None

    # for_statement: for_condition | for_initialization_declaration | for_range;
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        if ctx.for_condition():
            return self.visit(ctx.for_condition())
        elif ctx.for_initialization_declaration():
            return self.visit(ctx.for_initialization_declaration())
        elif ctx.for_range():
            return self.visit(ctx.for_range())

    # for_condition: FOR expression1 LBRACEBRACK statement_list RBRACEBRACK;
    def visitFor_condition(self, ctx:MiniGoParser.For_conditionContext):
        cond = self.visit(ctx.expression1())
        loop = Block(self.visit(ctx.statement_list()))
        return ForBasic(cond, loop)

    # for_assignment_statement: ID assign_operator expression1;
    def visitFor_assignment_statement(self, ctx:MiniGoParser.For_assignment_statementContext):
        lhs = Id(ctx.ID().getText())
        op = ctx.assign_operator().getText()
        rhs = self.visit(ctx.expression1())
        if op == ':=':
            return Assign(lhs, rhs)
        elif op == '+=':
            return Assign(lhs, BinaryOp('+', lhs, rhs))
        elif op == '-=':
            return Assign(lhs, BinaryOp('-', lhs, rhs))
        elif op == '*=':
            return Assign(lhs, BinaryOp('*', lhs, rhs))
        elif op == '/=':
            return Assign(lhs, BinaryOp('/', lhs, rhs))
        elif op == '%=':
            return Assign(lhs, BinaryOp('%', lhs, rhs))

    # for_variable_declared_statement: VAR ID optional_type required_initial_expression;
    def visitFor_variable_declared_statement(self, ctx:MiniGoParser.For_variable_declared_statementContext):
        var_name = ctx.ID().getText()
        var_type = self.visit(ctx.optional_type())
        if isinstance(var_type, VoidType):
            var_type = None
        var_init = self.visit(ctx.required_initial_expression())
        return VarDecl(var_name, var_type, var_init)

    # for_initialization_declaration: FOR (for_assignment_statement | for_variable_declared_statement) end_statement expression1 end_statement for_assignment_statement LBRACEBRACK statement_list RBRACEBRACK;
    def visitFor_initialization_declaration(self, ctx:MiniGoParser.For_initialization_declarationContext):
        assignment_stmts = ctx.for_assignment_statement()
        if len(assignment_stmts) == 2:
            init = self.visit(assignment_stmts[0])
            upda = self.visit(assignment_stmts[1])
        else:
            init = self.visit(ctx.for_variable_declared_statement())
            upda = self.visit(assignment_stmts[0])
        cond = self.visit(ctx.expression1())
        loop = Block(self.visit(ctx.statement_list()))
        return ForStep(init, cond, upda, loop)

    # for_range: FOR ID COMMA ID assign_operator RANGE expression1 LBRACEBRACK statement_list RBRACEBRACK;
    def visitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        idx = Id(ctx.ID(0).getText())
        value = Id(ctx.ID(1).getText())
        arr = self.visit(ctx.expression1())
        loop = Block(self.visit(ctx.statement_list()))
        return ForEach(idx, value, arr, loop)

    # call_statement: function_call_statement | method_call_statement;
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        if ctx.function_call_statement():
            return self.visit(ctx.function_call_statement())
        elif ctx.method_call_statement():
            return self.visit(ctx.method_call_statement())

    # function_call_statement: ID LPAREN expression_list RPAREN;
    def visitFunction_call_statement(self, ctx:MiniGoParser.Function_call_statementContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.expression_list()))

    # method_call_statement: lhs DOT ID LPAREN expression_list RPAREN;
    def visitMethod_call_statement(self, ctx:MiniGoParser.Method_call_statementContext):
        receiver = self.visit(ctx.lhs())
        method_name = ctx.ID().getText()
        args = self.visit(ctx.expression_list())
        return MethCall(receiver, method_name, args)

    # function_declared_statement: FUNC ID LPAREN optional_parameter_list RPAREN optional_type LBRACEBRACK statement_list RBRACEBRACK;
    def visitFunction_declared_statement(self, ctx:MiniGoParser.Function_declared_statementContext):
        return FuncDecl(ctx.ID().getText(), self.visit(ctx.optional_parameter_list()), self.visit(ctx.optional_type()), Block(self.visit(ctx.statement_list())))

    # method_declared_statement: FUNC method_receiver ID LPAREN optional_parameter_list RPAREN optional_type LBRACEBRACK statement_list RBRACEBRACK;
    def visitMethod_declared_statement(self, ctx:MiniGoParser.Method_declared_statementContext):
        receiver, receive_type = self.visit(ctx.method_receiver())
        body_method = FuncDecl(ctx.ID().getText(), self.visit(ctx.optional_parameter_list()), self.visit(ctx.optional_type()), Block(self.visit(ctx.statement_list())))
        return MethodDecl(receiver, receive_type, body_method)

    # method_receiver: LPAREN ID ID RPAREN;
    def visitMethod_receiver(self, ctx:MiniGoParser.Method_receiverContext):
        return ctx.ID(0).getText(), Id(ctx.ID(1).getText())

    # struct_declared_statement: TYPE ID STRUCT LBRACEBRACK list_field_declared_statement RBRACEBRACK;
    def visitStruct_declared_statement(self, ctx:MiniGoParser.Struct_declared_statementContext):
        return StructType(ctx.ID().getText(), self.visit(ctx.list_field_declared_statement()), [])

    # list_field_declared_statement: field_declared_statement list_field_declared_statement | field_declared_statement;
    def visitList_field_declared_statement(self, ctx:MiniGoParser.List_field_declared_statementContext):
        if ctx.list_field_declared_statement():
            return [self.visit(ctx.field_declared_statement())] + self.visit(ctx.list_field_declared_statement())
        return [self.visit(ctx.field_declared_statement())]

    # field_declared_statement: ID required_type end_statement;
    def visitField_declared_statement(self, ctx:MiniGoParser.Field_declared_statementContext):
        return (ctx.ID().getText(), self.visit(ctx.required_type()))

    # function_interface_declared_statement: ID LPAREN optional_parameter_list RPAREN optional_type end_statement;
    def visitFunction_interface_declared_statement(self, ctx:MiniGoParser.Function_interface_declared_statementContext):
        list_type = [param.parType for param in self.visit(ctx.optional_parameter_list())]
        return Prototype(ctx.ID().getText(), list_type, self.visit(ctx.optional_type()))

    # list_function_declared_interface: function_interface_declared_statement list_function_declared_interface | function_interface_declared_statement;
    def visitList_function_declared_interface(self, ctx:MiniGoParser.List_function_declared_interfaceContext):
        if ctx.list_function_declared_interface():
            return [self.visit(ctx.function_interface_declared_statement())] + self.visit(ctx.list_function_declared_interface())
        return [self.visit(ctx.function_interface_declared_statement())]

    # interface_declared_statement: TYPE ID INTERFACE LBRACEBRACK list_function_declared_interface RBRACEBRACK;
    def visitInterface_declared_statement(self, ctx:MiniGoParser.Interface_declared_statementContext):
        return InterfaceType(ctx.ID().getText(), self.visit(ctx.list_function_declared_interface()))