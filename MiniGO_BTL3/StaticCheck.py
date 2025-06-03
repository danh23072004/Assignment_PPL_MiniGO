# 2210458
import AST
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Tuple

# from StaticError import Prototype as StaticPrototype
from StaticError import Type as StaticErrorType
from AST import Type

class FunctionType(Type):
    def __str__(self):
        return "FunctionType"

    def accept(self, v, param):
        return v.visitFuntionType(self, param)


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + (
            "" if self.value is None else "," + str(self.value)) + ")"

# This is a class especially for the NilLiteral that I created myself
@dataclass()
class NilType(Type):
    def __str__(self):
        return "NilType"

    def accept(self, v, param):
        return v.visitNilType(self, param)


def evaluateAST(ast: AST, c: List[List[Symbol]]) -> int:
    if isinstance(ast, AST.IntLiteral):
        return ast.value
    elif isinstance(ast, AST.Id):
        for sublist in c:
            res: Symbol = next(filter(lambda x: x.name == ast.name, sublist), None)
            if res and isinstance(res.mtype, IntType):
                return res.value
    elif isinstance(ast, AST.BinaryOp):
        left = evaluateAST(ast.left, c)
        right = evaluateAST(ast.right, c)

        if (left is None and isinstance(right, IntLiteral)) or (right is None and isinstance(left, IntLiteral)):
            raise TypeMismatch(ast)

        if (not isinstance(left, int)) or (not isinstance(right, int)):
            return None
        if ast.op == '+':
            return left + right
        elif ast.op == '*':
            return left * right
        elif ast.op == '-':
            return left - right
        elif ast.op == '/':
            return left // right
        elif ast.op == '%':
            return left % right
    elif isinstance(ast, AST.UnaryOp):
        operand = evaluateAST(ast.body, c)
        if operand is None:
            return None
        if ast.op == '+':
            return +operand
        elif ast.op == '-':
            return -operand


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.list_type: List[Union[StructType, InterfaceType]] = []
        self.list_function: List[FuncDecl] = []
        self.built_in_function: List[FuncDecl] = [
            FuncDecl("getInt", [], IntType(), Block([])),
            FuncDecl("putInt", [ParamDecl("i", IntType())], VoidType(), Block([])),
            FuncDecl("putIntLn", [ParamDecl("i", IntType())], VoidType(), Block([])),
            FuncDecl("getFloat", [], FloatType(), Block([])),
            FuncDecl("putFloat", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            FuncDecl("putFloatLn", [ParamDecl("f", FloatType())], VoidType(), Block([])),
            FuncDecl("getBool", [], BoolType(), Block([])),
            FuncDecl("putBool", [ParamDecl("b", BoolType())], VoidType(), Block([])),
            FuncDecl("putBoolLn", [ParamDecl("b", BoolType())], VoidType(), Block([])),
            FuncDecl("getString", [], StringType(), Block([])),
            FuncDecl("putString", [ParamDecl("s", StringType())], VoidType(), Block([])),
            FuncDecl("putStringLn", [ParamDecl("s", StringType())], VoidType(), Block([])),
            FuncDecl("putLn", [], VoidType(), Block([])),
        ]
        self.function_current: FuncDecl = None


    def check(self):
        self.visit(self.ast, None)

    def compareInterfaceLHS_StructTypeRHS(self, lhs_type: InterfaceType, rhs_type: StructType) -> bool:
        if not (isinstance(lhs_type, InterfaceType) and isinstance(rhs_type, StructType)):
            return False
        # if len(lhs_type.methods) != len(rhs_type.methods):
        #     return False

        for prototype in lhs_type.methods:
            for method in rhs_type.methods:
                if prototype.name == method.fun.name:
                    if len(prototype.params) != len(method.fun.params):
                        return False
                    for i in range(len(prototype.params)):
                        if not ((type(prototype.params[i]) == type(method.fun.params[i].parType)) and prototype.params[i] == method.fun.params[i].parType):
                            return False
                    if not ((type(prototype.retType) == type(method.fun.retType)) and prototype.retType == method.fun.retType):
                        return False

        for prototype in lhs_type.methods:
            method: MethodDecl = self.lookup(prototype.name, rhs_type.methods, lambda x: x.fun.name)
            if method is None:
                return False
            if len(prototype.params) != len(method.fun.params):
                return False
            for i in range(len(prototype.params)):
                if not ((type(prototype.params[i]) == type(method.fun.params[i].parType)) and prototype.params[i] == method.fun.params[i].parType):
                    return False
            if not ((type(prototype.retType) == type(method.fun.retType)) and prototype.retType == method.fun.retType):
                return False
        return True

    # The result of evaluation is only of type int

    # This function is only used for assignment statement or variable or constant declaration
    def checkType(self, lhs_type: Type, rhs_type: Type, list_type_permission: List[Tuple[Type, Type]] = [], c: List[List[Symbol]] = []) -> bool:
        list_type_permission = list_type_permission + [
            (FloatType, IntType), (InterfaceType, StructType), (InterfaceType, NilType), (StructType, NilType)]

        # Covert from Id to StructType or InterfaceType
        lhs_type = self.lookup(lhs_type.name, self.list_type, lambda x: x.name) if isinstance(lhs_type, Id) else lhs_type
        rhs_type = self.lookup(rhs_type.name, self.list_type, lambda x: x.name) if isinstance(rhs_type, Id) else rhs_type

        # For array type validation
        if isinstance(lhs_type, ArrayType) and isinstance(rhs_type, ArrayType):

            if len(lhs_type.dimens) != len(rhs_type.dimens):
                return False

            # Calculate and compare value of each dimension
            for d1, d2 in zip(lhs_type.dimens, rhs_type.dimens):
                value_1: int = evaluateAST(d1, c)
                value_2: int = evaluateAST(d2, c)
                if value_1 != value_2:
                    return False

        lhs_type = lhs_type.eleType if isinstance(lhs_type, ArrayType) else lhs_type
        rhs_type = rhs_type.eleType if isinstance(rhs_type, ArrayType) else rhs_type

        # For scalar type or element type of array type
        if (type(lhs_type), type(rhs_type)) in list_type_permission:
            if isinstance(lhs_type, FloatType) and isinstance(rhs_type, IntType):
                return True

            # validate if struct type equal interface type (struct type implements all prototypes of interface type)
            if isinstance(lhs_type, InterfaceType) and isinstance(rhs_type, StructType):
                return self.compareInterfaceLHS_StructTypeRHS(lhs_type, rhs_type)
            return True

        # To check if the type is equal
        if type(lhs_type) == type(rhs_type):
            # If lhs_type is a struct type and rhs_type is a struct type, check if both implements are the same
            return lhs_type == rhs_type
        return False

    def getAllDeclsNameAndType(self, ast: Program) -> List[Tuple[str, Union[Decl, Type]]]:
        # Get all declarations (function, variable declared, constant declared, struct type, interface type) in the program
        list_name: list[Tuple[str, Union[Decl, Type]]] = []
        # append built_in_function name to list_name
        # list_name += [ele.name for ele in self.built_in_function]
        for ele in ast.decl:
            if isinstance(ele, VarDecl):
                list_name.append((ele.varName, ele))
            elif isinstance(ele, ConstDecl):
                list_name.append((ele.conName, ele))
            elif isinstance(ele, FuncDecl):
                list_name.append((ele.name, ele))
            elif isinstance(ele, StructType) or isinstance(ele, InterfaceType):
                list_name.append((ele.name, ele))
        return list_name

    def visitProgram(self, ast: Program, c: None):
        # This part is used for adding method declarations to the struct
        def visitMethodDecl(ast: MethodDecl, c: StructType) -> MethodDecl:
            res = self.lookup(ast.fun.name, c.methods, lambda x: x.fun.name)
            if not res is None:
                raise Redeclared(Method(), ast.fun.name)

            res = self.lookup(ast.fun.name, c.elements, lambda x: x[0])
            if not res is None:
                raise Redeclared(Method(), ast.fun.name)

            # add the method to the struct
            c.methods.append(ast)

            return ast



        # get list of all type declarations including struct and interface, also check if there is any duplicate type
        self.list_type = reduce(lambda acc, ele: [self.visit(ele, self.getAllDeclsNameAndType(ast))] + acc if isinstance(ele, Type) else acc, ast.decl, [])


        # get the list of all function declarations
        self.list_function = self.built_in_function + list(filter(lambda item: isinstance(item, FuncDecl), ast.decl))

        # This following code add MethodDecl to the following struct type
        receiver_type = list(map(
            lambda item: visitMethodDecl(item, self.lookup(item.recType.name, self.list_type, lambda x: x.name)),
            list(filter(lambda item: isinstance(item, MethodDecl), ast.decl))
        ))


        list_builtin_function: list[Symbol] = [
                reduce (lambda acc, ele: [Symbol(ele.name, FunctionType(), None)] + acc, self.built_in_function, [])
            ]



        # Check all type declarations (in list_type) whether they have the same name in list_decl_with_builtin_function or not
        # If they have the same name, raise a redeclared error
        for ele in self.list_type:
            res = self.lookup(ele.name, list_builtin_function[0], lambda x: x.name)
            if not res is None:
                raise Redeclared(StaticErrorType(), ele.name)


        test = reduce(
            lambda acc, ele:
            [([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]] + acc[1:],
            filter(lambda item: isinstance(item, Decl), ast.decl),
            list_builtin_function
        )

    def visitStructType(self, ast: StructType, list_decl: List[Tuple[str, Union[Decl, Type]]]) -> StructType:
        count: int = 0
        for decl in list_decl:
            if decl[0] == ast.name:
                count += 1
            if count == 2:
                if isinstance(decl[1], StructType) or isinstance(decl[1], InterfaceType):
                    raise Redeclared(StaticErrorType(), ast.name)
                elif isinstance(decl[1], FuncDecl):
                    raise Redeclared(Function(), ast.name)
                elif isinstance(decl[1], VarDecl):
                    raise Redeclared(Variable(), ast.name)
                elif isinstance(decl[1], ConstDecl):
                    raise Redeclared(Constant(), ast.name)

        # To visit field inside the struct
        def visitElements(element: Tuple[str, Type], c: List[Tuple[str, Type]]) -> Tuple[str, Type]:
            res = self.lookup(element[0], c, lambda x: x[0])
            if not res is None:
                raise Redeclared(Field(), element[0])
            return element

        ast.elements = reduce(lambda acc, ele: [visitElements(ele, acc)] + acc, ast.elements, [])
        return ast

    def visitPrototype(self, ast: AST.Prototype, c: List[Prototype]) -> Prototype:
        res = self.lookup(ast.name, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Prototype(), ast.name)
        return ast

    def visitInterfaceType(self, ast: InterfaceType, list_decl: List[Tuple[str, Union[Decl, Type]]]) -> InterfaceType:
        count: int = 0
        for decl in list_decl:
            if decl[0] == ast.name:
                count += 1
            if count == 2:
                if isinstance(decl[1], StructType) or isinstance(decl[1], InterfaceType):
                    raise Redeclared(StaticErrorType(), ast.name)
                elif isinstance(decl[1], FuncDecl):
                    raise Redeclared(Function(), ast.name)
                elif isinstance(decl[1], VarDecl):
                    raise Redeclared(Variable(), ast.name)
                elif isinstance(decl[1], ConstDecl):
                    raise Redeclared(Constant(), ast.name)

        ast.methods = reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.methods, [])
        return ast

    def visitFuncDecl(self, ast: FuncDecl, c: List[List[Symbol]]) -> Symbol:
        # Check if it exists
        res = self.lookup(ast.name, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)

        # This is further used for checking the return type
        self.function_current = ast


        # Create an empty list to store symbols for parameters
        param_symbols = []

        # Iterate over each parameter in ast.params
        for param in ast.params:
            # Visit the parameter to get a Symbol and prepend it to param_symbols
            symbol = self.visit(param, param_symbols)
            param_symbols.insert(0, symbol)

        # Create a new scope with the param_symbols and combine with existing context c
        new_context = [param_symbols] + c

        # Visit the function body with the new context
        self.visit(ast.body, new_context)
        # After visiting the function body, clear the current function
        self.function_current = None

        return Symbol(ast.name, ast.retType, None)

    def visitParamDecl(self, ast: ParamDecl, c: List[Symbol]) -> Symbol:
        res = self.lookup(ast.parName, c, lambda x: x.name)
        if not res is None:
            raise Redeclared(Parameter(), ast.parName)

        return Symbol(ast.parName, ast.parType, None)

    def visitMethodDecl(self, ast: MethodDecl, c: List[List[Symbol]]) -> None:
        # res = self.lookup(ast.fun.name, c[0], lambda x: x.name)
        # if not res is None:
        #     raise Redeclared(Function(), ast.name)

        scope = [[Symbol(ast.receiver, ast.recType, None)]] + c

        # This is further used for checking the return type
        self.function_current = ast.fun

        # Initialize the accumulator as an empty list
        acc = []

        # Iterate over each parameter in ast.fun.params
        for ele in ast.fun.params:
            # Visit the element with the current accumulator and prepend the result
            visited = self.visit(ele, acc)
            acc = [visited] + acc

        # Combine the result with the scope and visit the function body
        result = self.visit(ast.fun.body, [acc] + scope)

        # After visiting the function body, clear the current function
        self.function_current = None

        # return Symbol(ast.fun.name, ast.fun.retType, None)



    def visitVarDecl(self, ast: VarDecl, c: List[List[Symbol]]) -> Symbol:
        # Check redeclared
        res = self.lookup(ast.varName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName)

        # Get type of both lhs and rhs
        lhs_type = (self.lookup(ast.varType.name, self.list_type, lambda x: x.name)
            if isinstance(ast.varType, Id)
            else ast.varType
        ) if ast.varType else None
        rhs_type: Type = self.visit(ast.varInit, c) if ast.varInit else None

        if rhs_type is None:
            return Symbol(ast.varName, lhs_type, None)
        elif lhs_type is None:
            return Symbol(ast.varName, rhs_type, None)
        elif self.checkType(lhs_type, rhs_type, [], c):
            return Symbol(ast.varName, lhs_type, None)
        raise TypeMismatch(ast)

    def visitConstDecl(self, ast: ConstDecl, c: List[List[Symbol]]) -> Symbol:
        res = self.lookup(ast.conName, c[0], lambda x: x.name)
        if not res is None:
            raise Redeclared(Constant(), ast.conName)

        # get value of iniExpr
        ini_expr_value: int = evaluateAST(ast.iniExpr, c) if ast.iniExpr else None

        return Symbol(ast.conName, self.visit(ast.iniExpr, c) if ast.iniExpr else ast.conType, ini_expr_value)

    def visitBlock(self, ast: Block, c: List[List[Symbol]]) -> None:
        acc = [[]] + c

        for ele in ast.member:
            # the code: isinstance(ele, (FuncCall, MethCall)) => to determine the function/method call used in a block is a statement
            result = None
            if isinstance(ele, (FuncCall, MethCall)):
                result = self.visit(ele, (acc, True))
            elif not isinstance(ele, Symbol):
                result = self.visit(ele, acc)
            else:
                result = ele

            # result = self.visit(ele, acc) if not isinstance(ele, Symbol) else ele

            if isinstance(result, Symbol):
                acc[0] = [result] + acc[0]



    def visitForBasic(self, ast: ForBasic, c: List[List[Symbol]]) -> None:
        cond_type: Type = self.visit(ast.cond, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)
        self.visit(Block(ast.loop.member), c)

    def visitForStep(self, ast: ForStep, c: List[List[Symbol]]) -> None:
        # Create a fake scope for the initialization statement
        c.insert(0, [])  # Add a new scope for the initialization statement

        # Visit the initialization statement first
        init_result = self.visit(ast.init, c)

        # If a Symbol is returned (e.g., from VarDecl), add it to the current scope
        if isinstance(init_result, Symbol):
            c[0].insert(0, init_result)  # Add to the front of the current scope

        # Check the condition type
        cond_type: Type = self.visit(ast.cond, c)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)

        # Remove the fake scope for the initialization statement
        c.pop(0)  # Remove the fake scope

        # Visit the update statement
        self.visit(Block([ast.init] + [ast.upda] + ast.loop.member), c)

    def visitForEach(self, ast: ForEach, c: List[List[Symbol]]) -> None:
        # Visit the array expression and check its type
        array_type: ArrayType = self.visit(ast.arr, c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)

        # Check if ast.idx is available in the whole program or not
        # If not, raise Undeclared error
        idx: Symbol = None
        for scope in c:
            idx: Symbol = self.lookup(ast.idx.name, scope, lambda x: x.name)
            if idx is not None: break
        if idx is None:
            raise Undeclared(Identifier(), ast.idx.name)

        if not isinstance(idx.mtype, IntType):
            raise TypeMismatch(ast)


        # Check if ast.value is available in the whole program or not
        # If not, raise Undeclared error
        value: Symbol = None
        for scope in c:
            value: Symbol = self.lookup(ast.value.name, scope, lambda x: x.name)
            if value is not None: break
        if value is None:
            raise Undeclared(Identifier(), ast.value.name)

        # Index (ast.idx) is always IntType
        idx_symbol = Symbol(ast.idx.name, IntType(), None)


        # Value (ast.value) takes the element type of the array
        if len(array_type.dimens) == 1:
            value_symbol = Symbol(ast.value.name, array_type.eleType, None)
        else:
            value_symbol = Symbol(ast.value.name, ArrayType(array_type.dimens[1:], array_type.eleType), None)

        # Step 4: Create a new scope with idx and value, then visit the loop body
        self.visit(Block(ast.loop.member), c)

    def visitId(self, ast: Id, c: List[List[Symbol]]) -> Type:
        for sublist in c:  # Iterate over all sublists in c
            res: Symbol = next(filter(lambda x: x.name == ast.name, sublist), None)
            if res and not isinstance(res.mtype, Function):
                return res.mtype if not isinstance(res.mtype, Id) else self.lookup(res.mtype.name, self.list_type, lambda x: x.name)
        raise Undeclared(Identifier(), ast.name)

    def visitFieldAccess(self, ast: FieldAccess, c: List[List[Symbol]]) -> Type:
        type_receiver: Type = self.visit(ast.receiver, c)
        # If the receiver is not a struct type, raise a type mismatch because a scalar type doesn't have fields
        if not isinstance(type_receiver, StructType):
            raise TypeMismatch(ast)
        # Find the field in the struct type
        res = self.lookup(ast.field, type_receiver.elements if isinstance(type_receiver, StructType) else None, lambda x: x[0])
        if res is None:
            raise Undeclared(Field(), ast.field)
        return res[1] if not isinstance(res[1], Id) else self.lookup(res[1].name, self.list_type, lambda x: x.name)

    def resolve_type(self, typ: Type) -> Type:
        if isinstance(typ, Id):
            actual_typ = self.lookup(typ.name, self.list_type, lambda x: x.name)
            if actual_typ is None:
                raise Undeclared(Type(), typ.name)
            return actual_typ
        return typ

    def checkCall(self, ast, param_types: List[Type], args: List[Expr], ret_type: Type, is_stmt: bool,
                  c: List[List[Symbol]]) -> Type:
        resolved_param_types = [self.resolve_type(pt) for pt in param_types]
        if len(resolved_param_types) != len(args):
            raise TypeMismatch(ast)
        for param_type, arg in zip(resolved_param_types, args):
            arg_type = self.visit(arg, c)
            if not isinstance(arg_type, NilType):
                # Validate the type of the argument if the argument's type is AST.ArrayType
                if isinstance(arg_type, AST.ArrayType) and isinstance(param_type, AST.ArrayType):
                    if not (
                        (len(arg_type.dimens) == len(param_type.dimens)) and
                        (type(arg_type.eleType) == type(param_type.eleType)) and
                        (arg_type.eleType == param_type.eleType)
                    ):
                        raise TypeMismatch(ast)
                    # Validate each dimension of the array if they are equal or not
                    for index_arg_type, index_param_type in zip(arg_type.dimens, param_type.dimens):
                        value_1: int = evaluateAST(index_arg_type, c)
                        value_2: int = evaluateAST(index_param_type, c)
                        if value_1 != value_2:
                            raise TypeMismatch(ast)
                # Validate types other than Array Type
                elif not (type(arg_type) == type(param_type) and arg_type == param_type):
                    raise TypeMismatch(ast)
        resolved_ret_type = self.resolve_type(ret_type)
        if not is_stmt and isinstance(resolved_ret_type, VoidType):
            raise TypeMismatch(ast)
        if is_stmt and not isinstance(resolved_ret_type, VoidType):
            raise TypeMismatch(ast)
        return resolved_ret_type

    def visitFuncCall(self, ast: FuncCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, Tuple):
            c, is_stmt = c

        if len(c) > 3:
            for i in range (0, 3):
                res = self.lookup(ast.funName, c[i], lambda x: x.name)
                if res:
                    raise Undeclared(Function(), ast.funName)
        elif len(c) == 3:
            for i in range (0, 2):
                res = self.lookup(ast.funName, c[i], lambda x: x.name)
                if res:
                    raise Undeclared(Function(), ast.funName)

        function = self.lookup(ast.funName, self.list_function, lambda x: x.name)
        if not function:
            raise Undeclared(Function(), ast.funName)

        param_types = [param.parType for param in function.params]
        ret_type = function.retType
        return self.checkCall(ast, param_types, ast.args, ret_type, is_stmt, c)

    def visitMethCall(self, ast: MethCall, c: Union[List[List[Symbol]], Tuple[List[List[Symbol]], bool]]) -> Type:
        is_stmt = False
        if isinstance(c, Tuple):
            c, is_stmt = c

        type_receiver: Type = self.visit(ast.receiver, c)
        method = None
        if isinstance(type_receiver, StructType):
            method: MethodDecl = self.lookup(ast.metName, type_receiver.methods, lambda x: x.fun.name)
        elif isinstance(type_receiver, InterfaceType):
            method: Prototype = self.lookup(ast.metName, type_receiver.methods, lambda x: x.name)
        else:
            raise TypeMismatch(ast)

        if not method:
            raise Undeclared(Method(), ast.metName)

        if isinstance(method, AST.MethodDecl):
            param_types = [param.parType for param in method.fun.params]
            ret_type = method.fun.retType
        elif isinstance(method, AST.Prototype):
            param_types = method.params
            ret_type = method.retType

        return self.checkCall(ast, param_types, ast.args, ret_type, is_stmt, c)

    def visitIntType(self, ast, param):
        return None

    def visitFloatType(self, ast, param):
        return None

    def visitBoolType(self, ast, param):
        return None

    def visitStringType(self, ast, param):
        return None

    def visitVoidType(self, ast, param):
        return None

    def visitArrayType(self, ast: ArrayType, c: List[List[Symbol]]) -> Type:
        for index in ast.dimens:
            index_type = self.visit(index, c)
            if not isinstance(index_type, IntType):
                raise TypeMismatch(ast)
        return ast

    # Return Symbol if the variable has not been declared yet
    # Return Type in case of a field access
    # Return None if the variable has been declared
    def visitAssign(self, ast: Assign, c: List[List[Symbol]]) -> Symbol:
        lhs = None
        for sublist in c:
            # Check if the variable is already declared or not
            if isinstance(ast.lhs, Id):
                lhs: Symbol = self.lookup(ast.lhs.name, sublist, lambda x: x.name)
                if lhs is not None:
                    break
            elif isinstance(ast.lhs, FieldAccess) or isinstance(ast.lhs, ArrayCell):
                lhs = self.visit(ast.lhs, c)
        if lhs is None:
            # If the variable is not declared, declare it and add it to the list of symbols
            lhs = Symbol(ast.lhs.name, self.visit(ast.rhs, c))
            return lhs

        # This part is not completely implemented yet (for the part mismatch type)
        if isinstance(lhs, Symbol):
            # If the lhs is a function, raise a type mismatch
            if isinstance(lhs.mtype, Function):
                raise TypeMismatch(ast.lhs)
            if not self.checkType(lhs.mtype, self.visit(ast.rhs, c), [], c):
                raise TypeMismatch(ast)
            return lhs.mtype
        elif isinstance(lhs, Type):
            # If the lhs is a type, check if the type is equal to the rhs type
            if not self.checkType(lhs, self.visit(ast.rhs, c), [], c):
                raise TypeMismatch(ast)
            return lhs

    def visitIf(self, ast: If, c: List[List[Symbol]]) -> None:
        expr_type: Type = self.visit(ast.expr, c)
        if not isinstance(expr_type, BoolType):
            raise TypeMismatch(ast)
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            self.visit(ast.elseStmt, c)
        return None

    def visitContinue(self, ast, param):
        return None

    def visitBreak(self, ast, param):
        return None

    def visitReturn(self, ast: Return, c: List[List[Symbol]]) -> None:
        return_type: Type = self.visit(ast.expr, c) if ast.expr else VoidType()
        function_current_type: Type = self.lookup(self.function_current.retType.name, self.list_type, lambda x: x.name) if isinstance(self.function_current.retType, Id) else self.function_current.retType
        # This validation can't use checkType because checkType is only used for statement

        # Allow return nil in function and method
        if isinstance(return_type, NilType):
            return

        # validate ArrayType first
        if isinstance(return_type, ArrayType) and isinstance(function_current_type, ArrayType):
            if ((len(return_type.dimens) != len(function_current_type.dimens)) or
                (type(return_type.eleType) != type(function_current_type.eleType))):
                raise TypeMismatch(ast)
        # validate scalar type, struct type or interface type
        elif type(return_type) != type(function_current_type) or return_type != function_current_type:
            raise TypeMismatch(ast)


    def visitBinaryOp(self, ast: BinaryOp, c: List[List[Symbol]]) -> Type:
        lhs_type: Type = self.visit(ast.left, c)
        rhs_type: Type = self.visit(ast.right, c)

        if ast.op in ['+', '-', '*', '/']:
            if type(lhs_type) == BoolType or type(rhs_type) == BoolType:
                raise TypeMismatch(ast)
            if ((type(lhs_type) == StringType and type(rhs_type) != StringType) or
                    (type(rhs_type) == StringType and type(lhs_type) != StringType)):
                raise TypeMismatch(ast)
            elif type(lhs_type) == StringType:
                return StringType()
            elif type(lhs_type) == FloatType or type(rhs_type) == FloatType:
                return FloatType()
            elif type(lhs_type) == IntType:
                return IntType()

        if ast.op in ['%']:
            if type(lhs_type) == IntType and type(rhs_type) == IntType:
                return IntType()

        if ast.op in ['&&', '||']:
            if type(lhs_type) == BoolType and type(rhs_type) == BoolType:
                return BoolType()

        if ast.op in ['>', '<', '>=', '<=', '==', '!=']:
            if (type(lhs_type) == type(rhs_type)) and (lhs_type == rhs_type):
                return BoolType()

        raise TypeMismatch(ast)

    def visitUnaryOp(self, ast: UnaryOp, c: List[List[Symbol]]) -> Type:
        expr_type: Type = self.visit(ast.body, c)

        if ast.op in ['+', '-']:
            if isinstance(expr_type, FloatType):
                return FloatType()
            elif isinstance(expr_type, IntType):
                return IntType()
            else:
                raise TypeMismatch(ast)

        if ast.op in ['!']:
            if isinstance(expr_type, BoolType):
                return BoolType()
            else:
                raise TypeMismatch(ast)



    # This visit may return prime literal type or array type
    def visitArrayCell(self, ast: ArrayCell, c: List[List[Symbol]]) -> Type:
        for index in ast.idx:
            index_type: Type = self.visit(index, c)
            if not isinstance(index_type, IntType):
                raise TypeMismatch(ast)
        # Find the array type in the list of symbols
        array_type: ArrayType = self.visit(ast.arr, c)
        if not isinstance(array_type, ArrayType):
            raise TypeMismatch(ast)
        if len(array_type.dimens) == len(ast.idx):
            return array_type.eleType
        elif len(array_type.dimens) > len(ast.idx):
            array_element = ArrayType(array_type.dimens[len(ast.idx):], array_type.eleType)
            return array_element
        raise TypeMismatch(ast)

    def visitIntLiteral(self, ast, param) -> Type:
        return IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, c: List[List[Symbol]]) -> Type:
        return FloatType()

    def visitBooleanLiteral(self, ast: FloatLiteral, c: List[List[Symbol]]) -> Type:
        return BoolType()

    def visitStringLiteral(self, ast, param) -> Type:
        return StringType()

    def recursiveList(self, ast: NestedList, c: List[List[Symbol]]) -> None:
        for ele in ast:
            if isinstance(ele, list):
                self.recursiveList(ele, c)
            else:
                self.visit(ele, c)
        return None

    def visitArrayLiteral(self, ast: ArrayLiteral, c: List[List[Symbol]]):
        # Implement check elements type
        self.recursiveList(ast.value, c)
        return ArrayType(ast.dimens, ast.eleType)

    def visitStructLiteral(self, ast: StructLiteral, c: List[List[Symbol]]) -> Type:
        # Check if the struct type exists
        struct_type: StructType = self.lookup(ast.name, self.list_type, lambda x: x.name)
        if not struct_type:
            raise Undeclared(StaticErrorType(), ast.name)

        for field in ast.elements:
            # Check if the field name exists in the struct type
            field_name = self.lookup(field[0], struct_type.elements, lambda x: x[0])
            if not field_name:
                raise Undeclared(Field(), field[0])
            # Check if the field value is valid
            field_value = self.visit(field[1], c)
        return struct_type


    def visitNilLiteral(self, ast: NilLiteral, c: List[List[Symbol]]):
        return NilType()