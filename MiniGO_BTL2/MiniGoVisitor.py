# Generated from main/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#number.
    def visitNumber(self, ctx:MiniGoParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#grouped_expression.
    def visitGrouped_expression(self, ctx:MiniGoParser.Grouped_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression1.
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression2.
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression3.
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression4.
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression5.
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression6.
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression7.
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#final_expression.
    def visitFinal_expression(self, ctx:MiniGoParser.Final_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_list.
    def visitExpression_list(self, ctx:MiniGoParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression_part.
    def visitExpression_part(self, ctx:MiniGoParser.Expression_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal_inside_array.
    def visitLiteral_inside_array(self, ctx:MiniGoParser.Literal_inside_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_literal.
    def visitList_literal(self, ctx:MiniGoParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_part.
    def visitDimension_part(self, ctx:MiniGoParser.Dimension_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimension_list.
    def visitDimension_list(self, ctx:MiniGoParser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nested_array_element_list.
    def visitNested_array_element_list(self, ctx:MiniGoParser.Nested_array_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_nested_array_element_list.
    def visitList_nested_array_element_list(self, ctx:MiniGoParser.List_nested_array_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_element_list.
    def visitArray_element_list(self, ctx:MiniGoParser.Array_element_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_literal.
    def visitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_element.
    def visitField_element(self, ctx:MiniGoParser.Field_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_list.
    def visitField_list(self, ctx:MiniGoParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_literal.
    def visitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#end_statement.
    def visitEnd_statement(self, ctx:MiniGoParser.End_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#declared.
    def visitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement_list.
    def visitStatement_list(self, ctx:MiniGoParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#const_declared_statement.
    def visitConst_declared_statement(self, ctx:MiniGoParser.Const_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#required_type.
    def visitRequired_type(self, ctx:MiniGoParser.Required_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_type.
    def visitOptional_type(self, ctx:MiniGoParser.Optional_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#required_initial_expression.
    def visitRequired_initial_expression(self, ctx:MiniGoParser.Required_initial_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_initial_expression.
    def visitOptional_initial_expression(self, ctx:MiniGoParser.Optional_initial_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variable_declared_statement.
    def visitVariable_declared_statement(self, ctx:MiniGoParser.Variable_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#optional_parameter_list.
    def visitOptional_parameter_list(self, ctx:MiniGoParser.Optional_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#separated_parameter_list.
    def visitSeparated_parameter_list(self, ctx:MiniGoParser.Separated_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#grouped_parameter_list.
    def visitGrouped_parameter_list(self, ctx:MiniGoParser.Grouped_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#variable_list.
    def visitVariable_list(self, ctx:MiniGoParser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#return_statement.
    def visitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#break_statement.
    def visitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continue_statement.
    def visitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assign_operator.
    def visitAssign_operator(self, ctx:MiniGoParser.Assign_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MiniGoParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_statement.
    def visitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_in_else_if_statement.
    def visitIf_in_else_if_statement(self, ctx:MiniGoParser.If_in_else_if_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_if_statement_list.
    def visitElse_if_statement_list(self, ctx:MiniGoParser.Else_if_statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#else_statement.
    def visitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_statement.
    def visitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_condition.
    def visitFor_condition(self, ctx:MiniGoParser.For_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_assignment_statement.
    def visitFor_assignment_statement(self, ctx:MiniGoParser.For_assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_variable_declared_statement.
    def visitFor_variable_declared_statement(self, ctx:MiniGoParser.For_variable_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_initialization_declaration.
    def visitFor_initialization_declaration(self, ctx:MiniGoParser.For_initialization_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_range.
    def visitFor_range(self, ctx:MiniGoParser.For_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#call_statement.
    def visitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:MiniGoParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_call_statement.
    def visitMethod_call_statement(self, ctx:MiniGoParser.Method_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_declared_statement.
    def visitFunction_declared_statement(self, ctx:MiniGoParser.Function_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_declared_statement.
    def visitMethod_declared_statement(self, ctx:MiniGoParser.Method_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_receiver.
    def visitMethod_receiver(self, ctx:MiniGoParser.Method_receiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#struct_declared_statement.
    def visitStruct_declared_statement(self, ctx:MiniGoParser.Struct_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_field_declared_statement.
    def visitList_field_declared_statement(self, ctx:MiniGoParser.List_field_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_declared_statement.
    def visitField_declared_statement(self, ctx:MiniGoParser.Field_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#function_interface_declared_statement.
    def visitFunction_interface_declared_statement(self, ctx:MiniGoParser.Function_interface_declared_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#list_function_declared_interface.
    def visitList_function_declared_interface(self, ctx:MiniGoParser.List_function_declared_interfaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interface_declared_statement.
    def visitInterface_declared_statement(self, ctx:MiniGoParser.Interface_declared_statementContext):
        return self.visitChildren(ctx)



del MiniGoParser