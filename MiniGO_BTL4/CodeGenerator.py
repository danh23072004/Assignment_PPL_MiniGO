from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *
from typing import List, Tuple


class CodeGenerator(BaseVisitor, Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None
        self.arrayCellType = None
        self.list_type = {}
        self.struct: StructType = None

    def init(self):
        mem = [
            Symbol("putInt", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putIntLn", MType([IntType()], VoidType()), CName("io", True)),
            Symbol("putFloat", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putFloatLn", MType([FloatType()], VoidType()), CName("io", True)),
            Symbol("putString", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putStringLn", MType([StringType()], VoidType()), CName("io", True)),
            Symbol("putBool", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putBoolLn", MType([BoolType()], VoidType()), CName("io", True)),
            Symbol("putLn", MType([], VoidType()), CName("io", True)),
            Symbol("getInt", MType([], IntType()), CName("io", True)),
            Symbol("getFloat", MType([], FloatType()), CName("io", True)),
            Symbol("getString", MType([], StringType()), CName("io", True)),
            Symbol("getBool", MType([], BoolType()), CName("io", True))
        ]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)

    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False,
                                                frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.className), frame.getStartLabel(),
                                             frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", Id(self.className), 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def emitObjectCInit(self, ast: Program, env):
        frame = Frame("<cinit>", VoidType())
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        self.visit(Block([
            Assign(Id(item.varName if isinstance(item, VarDecl) else item.conName),
                   item.varInit if isinstance(item, VarDecl) else item.iniExpr)
            for item in ast.decl
            if isinstance(item, (VarDecl, ConstDecl))
        ]), env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitProgram(self, ast: Program, c):
        self.list_function = c + [
            Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className))
            for item in ast.decl if isinstance(item, FuncDecl)]
        self.list_type = {x.name: x for x in ast.decl if isinstance(x, Type)}
        for item in ast.decl:
            if type(item) is MethodDecl:
                self.list_type[item.recType.name].methods.append(item)
        env = {}
        env['env'] = [[]]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or isinstance(x, ConstDecl) else a,
                     ast.decl, env)
        # reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)
        gol = env['env'][0]
        env['env'] = [[]]
        for decl in ast.decl:
            if isinstance(decl, (VarDecl)):
                for item in gol:
                    if (decl.varName == item.name):
                        env['env'][0].append(item)
            if isinstance(decl, (ConstDecl)):
                for item in gol:
                    if (decl.conName == item.name):
                        env['env'][0].append(item)

            if isinstance(decl, FuncDecl):
                self.visit(decl, env)  # Không cập nhật env
        self.emitObjectInit()
        self.emitObjectCInit(ast, env)
        self.emit.printout(self.emit.emitEPILOG())

        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {
                'env': env['env']
            })
        return env

    ## TODO decl ------------------------------
    def visitFuncDecl(self, ast: FuncCall, o: dict) -> dict:
        self.function = ast
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None], StringType())], VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)

        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype, True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(
                self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None], StringType()), frame.getStartLabel(),
                                  frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc, e: self.visit(e, acc), ast.params, env)
        self.visit(ast.body, env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitParamDecl(self, ast: ParamDecl, o: dict) -> dict:
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(
            self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))
        return o

    def visitVarDecl(self, ast: VarDecl, o: dict) -> dict:
        def create_init(varType: Type, o: dict):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("\"\"")
            elif type(varType) is BoolType:
                return BooleanLiteral("false")
            elif type(varType) is Id:
                return StructLiteral(varType.name, [])
            elif type(varType) is ArrayType:
                shape = varType.dimens
                if len(shape) == 1:
                    return [create_init(varType.eleType, o) for _ in range(shape[0].value)]
                return [create_init(ArrayType(shape[1:], varType.eleType), o) for item in range(shape[0].value)]

        varInit = ast.varInit
        varType = ast.varType
        if not varInit:
            if type(varType) is ArrayType:
                varInit = ArrayLiteral(varType.dimens, varType.dimens, varType)
            else:
                varInit = create_init(varType, o)
            ast.varInit = varInit
        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType())
        rhsCode, rhsType = self.visit(varInit, env)
        if not varType:
            varType = rhsType

        if type(varType) is Id:
            varType = Id(varType.name)
        if 'frame' not in o:  # global var
            o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType, Index(index)))
            self.emit.printout(
                self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(o['frame'])
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index, frame))
        return o

    def visitFuncCall(self, ast: FuncCall, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.funName, self.list_function), None)
        if o.get('stmt'):
            o["stmt"] = False
            [self.emit.printout(self.visit(x, o)[0]) for x in ast.args]
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame']))
            return o
        output = "".join([str(self.visit(x, o)[0]) for x in ast.args])
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}", sym.mtype, o['frame'])
        return output, sym.mtype.rettype

    def visitBlock(self, ast: Block, o: dict) -> dict:
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))

        for item in ast.member:
            if type(item) is FuncCall or type(item) is MethCall:
                env["stmt"] = True
            env = self.visit(item, env)

        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o

    def visitId(self, ast: Id, o: dict) -> dict:
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]), None)

        if sym is None:
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR(ast.name, Id(self.struct.name), 0, o['frame']), Id(self.struct.name)
            return self.emit.emitREADVAR(ast.name, Id(self.struct.name), 0, o['frame']), Id(self.struct.name)

        if o.get('isLeft'):
            if type(sym.value) is Index:
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:
                return self.emit.emitPUTSTATIC(f"{self.className}/{sym.name}", sym.mtype, o['frame']), sym.mtype
        if type(sym.value) is Index:
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
        else:
            return self.emit.emitGETSTATIC(f"{self.className}/{sym.name}", sym.mtype, o['frame']), sym.mtype

    def visitAssign(self, ast: Assign, o: dict) -> dict:
        if type(ast.lhs) is Id and not next(filter(lambda x: x.name == ast.lhs.name, [j for i in o['env'] for j in i]),
                                            None):
            return self.visit(VarDecl(ast.lhs.name, None, ast.rhs), o)

        if type(ast.lhs) is FieldAccess:
            lhscode, typ = self.visit(ast.lhs.receiver, o)
            typ = self.list_type[typ.name]
            field = next(filter(lambda x: x[0] == ast.lhs.field, typ.elements), None)
            rhsCode, rhsType = self.visit(ast.rhs, o)
            if type(field[1]) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(o['frame'])
            self.emit.printout(lhscode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitPUTFIELD(f"{typ.name}/{field[0]}", field[1], o['frame']))
            return o
        elif type(ast.lhs) is ArrayCell:
            o['isLeft'] = True
            lhsCode, lhsType = self.visit(ast.lhs, o)
            o['isLeft'] = False
            rhsCode, rhsType = self.visit(ast.rhs, o)
            if type(lhsType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(o['frame'])
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitASTORE(self.arrayCell, o['frame']))
            return o

        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o)
        o['isLeft'] = False
        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode += self.emit.emitI2F(o['frame'])

        self.emit.printout(rhsCode)
        self.emit.printout(lhsCode)

        return o

    def visitReturn(self, ast: Return, o: dict) -> dict:
        if ast.expr:
            self.emit.printout(self.visit(ast.expr, o)[0])
        self.emit.printout(self.emit.emitRETURN(self.function.retType, o['frame']))
        return o

    ## TODO END decl ------------------------------

    ## TODO basic expression ------------------------------
    def visitBinaryOp(self, ast: BinaryOp, o: dict) -> tuple[str, Type]:
        op = ast.op
        frame = o['frame']
        if op in ['||']:
            label1 = frame.getNewLabel()
            label2 = frame.getNewLabel()
            codeLeft = self.visit(ast.left, o)[0] + self.emit.emitDUP(frame) + self.emit.emitIFFALSE(label1,
                                                                                                     frame) + self.emit.emitPUSHICONST(
                1, frame) + self.emit.emitGOTO(label2, frame)
            codeRight = self.emit.emitLABEL(label1, frame) + self.visit(ast.right, o)[0] + self.emit.emitLABEL(label2,
                                                                                                               frame)
            return codeLeft + codeRight + self.emit.emitOROP(frame), BoolType()
        if op in ['&&']:
            label1 = frame.getNewLabel()
            label2 = frame.getNewLabel()
            codeLeft = self.visit(ast.left, o)[0] + self.emit.emitDUP(frame) + self.emit.emitIFTRUE(label1,
                                                                                                    frame) + self.emit.emitPUSHICONST(
                0, frame) + self.emit.emitGOTO(label2, frame)
            codeRight = self.emit.emitLABEL(label1, frame) + self.visit(ast.right, o)[0] + self.emit.emitLABEL(label2,
                                                                                                               frame)
            return codeLeft + codeRight + self.emit.emitANDOP(frame), BoolType()

        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)
        if op in ['+', '-'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitADDOP(op, typeReturn, frame), typeReturn
        if op in ['*', '/']:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                if type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitMULOP(op, typeReturn, frame), typeReturn
        if op in ['%']:
            return codeLeft + codeRight + self.emit.emitMOD(frame), IntType()
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            return codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame), BoolType()

            # string
        if op in ['+', '-'] and type(typeLeft) in [StringType]:
            return codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat",
                                                                      MType([StringType()], StringType()),
                                                                      frame), StringType()
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            code = codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/compareTo",
                                                                      MType([StringType()], IntType()), frame)
            code = code + self.visit(IntLiteral(0), o)[0] + self.emit.emitREOP(op, IntType(), frame)
            return code, BoolType()

    def visitUnaryOp(self, ast: UnaryOp, o: dict) -> tuple[str, Type]:
        if ast.op == '!':
            code, type_return = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()

        code, type_return = self.visit(ast.body, o)
        return code + self.emit.emitNEGOP(type_return, o['frame']), type_return

    def visitIntLiteral(self, ast: IntLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), IntType()

    def visitFloatLiteral(self, ast: FloatLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHFCONST(ast.value, o['frame']), FloatType()

    def visitBooleanLiteral(self, ast: BooleanLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHICONST(ast.value, o['frame']), BoolType()

    def visitStringLiteral(self, ast: StringLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHCONST(ast.value, StringType(), o['frame']), StringType()

    ## TODO END basic expression ------------------------------

    ## TODO array ------------------------------
    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO['isLeft'] = False
        codeGen, arrType = self.visit(ast.arr, newO)

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCell = retType
        else:
            retType = ArrayType(arrType.dimens[len(ast.idx):], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame'])
            else:
                self.arrayCell = retType
        return codeGen, retType

    def visitArrayLiteral(self, ast: ArrayLiteral, o: dict) -> tuple[str, Type]:
        def nested2recursive(dat: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            if not isinstance(dat, list):
                return self.visit(dat, 0)

            frame = o['frame']
            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)
            if not isinstance(dat[0], list):
                _, type_element_array = self.visit(dat[0], o)
                codeGen += self.emit.emitNEWARRAY(type_element_array, frame)
                for idx, item in enumerate(dat):
                    codeGen += self.emit.emitDUP(frame)
                    codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                    codeGen += self.visit(item, o)[0]
                    codeGen += self.emit.emitASTORE(type_element_array, frame)
                return codeGen, ArrayType([IntLiteral(len(dat))], type_element_array)

            _, type_element_array = nested2recursive(dat[0], o)
            codeGen += self.emit.emitANEWARRAY(type_element_array, frame)
            for idx, item in enumerate(dat):
                codeGen += self.emit.emitDUP(frame)
                codeGen += self.emit.emitPUSHCONST(idx, IntType(), frame)
                codeGen += nested2recursive(item, o)[0]
                codeGen += self.emit.emitASTORE(type_element_array, frame)
            return codeGen, ArrayType([IntLiteral(len(dat))] + type_element_array.dimens, type_element_array.eleType)

        if type(ast.value) is ArrayType:
            return self.visit(ast.value, o)

        return nested2recursive(ast.value, o)

    ## TODO END array ------------------------------

    def visitConstDecl(self, ast: ConstDecl, o: dict) -> dict:
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)

    def visitArrayType(self, ast: ArrayType, o):
        codeGen = ""
        for item in ast.dimens:
            codeGen += self.visit(item, o)[0]
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])
        return codeGen, ast

    def visitIf(self, ast: If, o: dict) -> dict:
        frame = o['frame']
        label_exit = frame.getNewLabel()
        label_end_if = frame.getNewLabel()
        # if expr
        condCode, _ = self.visit(ast.expr, o)
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(label_end_if, frame))
        # visit body
        self.visit(ast.thenStmt, o)
        # goto exit
        self.emit.printout(self.emit.emitGOTO(label_exit, frame))
        # label end if
        self.emit.printout(self.emit.emitLABEL(label_end_if, frame))

        # else
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, o)

        # lable exit
        self.emit.printout(self.emit.emitLABEL(label_exit, frame))
        return o

    def visitForBasic(self, ast: ForBasic, o: dict) -> dict:
        frame = o['frame']
        frame.enterLoop()
        lable_new = frame.getNewLabel()
        lable_Break = frame.getBreakLabel()
        lable_Cont = frame.getContinueLabel()

        # label new
        self.emit.printout(self.emit.emitLABEL(lable_new, frame))

        # kiểm tra exp
        self.emit.printout(self.visit(ast.cond, o)[0])
        self.emit.printout(self.emit.emitIFFALSE(lable_Break, frame))

        # visit body
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(lable_Cont, frame))

        # goto lable_new
        self.emit.printout(self.emit.emitGOTO(lable_new, frame))

        # đặt lable_Break
        self.emit.printout(self.emit.emitLABEL(lable_Break, frame))

        # Exit loop
        frame.exitLoop()
        return o

    def visitForStep(self, ast: ForStep, o: dict) -> dict:

        env = o.copy()
        o['env'] = [[]] + o['env']
        o['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o['frame'].getStartLabel(), o['frame']))

        frame = o['frame']
        frame.enterLoop()
        lable_new = frame.getNewLabel()
        lable_Break = frame.getBreakLabel()
        lable_Cont = frame.getContinueLabel()

        o = self.visit(ast.init, o)

        # label new
        self.emit.printout(self.emit.emitLABEL(lable_new, frame))

        # kiểm tra exp
        self.emit.printout(self.visit(ast.cond, o)[0])
        self.emit.printout(self.emit.emitIFFALSE(lable_Break, frame))

        # visit body
        self.visit(ast.loop, o)
        self.emit.printout(self.emit.emitLABEL(lable_Cont, frame))

        self.visit(ast.upda, o)

        # goto lable_new
        self.emit.printout(self.emit.emitGOTO(lable_new, frame))

        # đặt lable_Break
        self.emit.printout(self.emit.emitLABEL(lable_Break, frame))

        # Exit loop
        frame.exitLoop()

        self.emit.printout(self.emit.emitLABEL(o['frame'].getEndLabel(), o['frame']))
        o['frame'].exitScope()

        return env

    def visitForEach(self, ast, o: dict) -> dict:
        return None

    def visitContinue(self, ast, o: dict) -> dict:
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))
        return o

    def visitBreak(self, ast, o: dict) -> dict:
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))
        return o

    ## TODO OOP ------------------------------
    def visitStructType(self, ast: StructType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))
        # .implements name
        for item in self.list_type.values():
            if type(item) is InterfaceType and self.checkType(item, ast, [(InterfaceType, StructType)]):
                self.emit.printout(f".implements {item.name}\n")

        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(f"public {item[0]}", item[1], False, False, False))

        self.visit(MethodDecl(None, None,
                              FuncDecl("<init>", [ParamDecl(item[0], item[1]) for item in ast.elements], VoidType(),
                                       Block([Assign(FieldAccess(Id("this"), item[0]), Id(item[0])) for item in
                                              ast.elements]))), o)

        self.visit(MethodDecl(None, None, FuncDecl("<init>", [], VoidType(), Block([]))), o)

        for item in ast.methods:
            self.visit(item, o)
        self.emit.printout(self.emit.emitEPILOG())

    def visitMethodDecl(self, ast: MethodDecl, o):
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)

        env = o.copy()
        env['frame'] = frame

        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype, False, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", Id(self.struct.name), frame.getStartLabel(),
                                             frame.getEndLabel(), frame))

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id(self.struct.name), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        index = 0
        for item in self.astTree.decl:
            if item == ast: break
            if isinstance(item, (VarDecl, ConstDecl)):
                index += 1
        env_g = env['env'][0][:index]

        env['env'] = [[]] + [env_g]

        env = reduce(lambda acc, e: self.visit(e, acc), ast.fun.params, env)
        self.visit(ast.fun.body, env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o

    def visitInterfaceType(self, ast: InterfaceType, o):
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))
        for item in ast.methods:
            self.emit.printout(
                self.emit.emitMETHOD(f"abstract {item.name}", MType([x for x in item.params], item.retType), False,
                                     None))
            self.emit.printout(".end method")
        self.emit.printout(self.emit.emitEPILOG())

    def visitFieldAccess(self, ast: FieldAccess, o: dict) -> tuple[str, Type]:
        code, typ = self.visit(ast.receiver, o)
        typ = self.list_type[typ.name]
        field = next(filter(lambda x: x[0] == ast.field, typ.elements), None)
        return code + self.emit.emitGETFIELD(f"{typ.name}/{ast.field}", field[1], o['frame']), field[1]

    def visitMethCall(self, ast: MethCall, o: dict) -> tuple[str, Type]:
        code, typ = self.visit(ast.receiver, o)
        typ = self.list_type[typ.name]

        is_stmt = o.pop("stmt", False)

        for arg in ast.args:
            arg_code, _ = self.visit(arg, o)
            code += arg_code
        returnType = None
        if isinstance(typ, StructType):
            method = next((m for m in typ.methods if m.fun.name == ast.metName), None)
            mtype = MType([param.parType for param in method.fun.params], method.fun.retType)
            returnType = method.fun.retType
            code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, o['frame'])

        elif isinstance(typ, InterfaceType):
            method = next((m for m in typ.methods if m.name == ast.metName), None)
            mtype = MType(method.params, method.retType)
            returnType = method.retType
            code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{ast.metName}", mtype, o['frame'])

        if is_stmt:
            self.emit.printout(code)
            return o

        return code, returnType

    def visitStructLiteral(self, ast: StructLiteral, o: dict) -> tuple[str, Type]:
        code = self.emit.emitNEW(ast.name, o['frame'])
        code += self.emit.emitDUP(o['frame'])
        list_type = []
        for item in ast.elements:
            c, t = self.visit(item[1], o)
            code += c
            list_type += [t]
        code += self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>",
                                            MType(list_type, VoidType()) if len(ast.elements) else MType([],
                                                                                                         VoidType()))
        return code, Id(ast.name)

    def visitNilLiteral(self, ast: NilLiteral, o: dict) -> tuple[str, Type]:
        return self.emit.emitPUSHNULL(o['frame']), Id("")

    def checkType(self, LSH_type: Type, RHS_type: Type, list_type_permission: List[Tuple[Type, Type]] = []) -> bool:
        if type(RHS_type) == StructType and RHS_type.name == "":
            return isinstance(LSH_type, (InterfaceType, StructType, Id))

        LSH_type = self.lookup(LSH_type.name, self.list_type.values(), lambda x: x.name) if isinstance(LSH_type,
                                                                                                       Id) else LSH_type
        RHS_type = self.lookup(RHS_type.name, self.list_type.values(), lambda x: x.name) if isinstance(RHS_type,
                                                                                                       Id) else RHS_type
        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                return all(
                    any(
                        struct_methods.fun.name == inteface_method.name and
                        self.checkType(struct_methods.fun.retType, inteface_method.retType) and
                        len(struct_methods.fun.params) == len(inteface_method.params) and
                        reduce(
                            lambda x, i: x and self.checkType(struct_methods.fun.params[i].parType,
                                                              inteface_method.params[i]),
                            range(len(struct_methods.fun.params)),
                            True
                        )
                        for struct_methods in RHS_type.methods
                    )
                    for inteface_method in LSH_type.methods
                )
            return True
        if isinstance(LSH_type, (InterfaceType, StructType)) and isinstance(RHS_type, (InterfaceType, StructType)):
            return LSH_type.name == RHS_type.name

        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            return (len(LSH_type.dimens) == len(RHS_type.dimens)
                    and all(
                        l.value == r.value for l, r in zip(LSH_type.dimens, RHS_type.dimens)
                    )
                    and self.checkType(LSH_type.eleType, RHS_type.eleType,
                                       [list_type_permission[0]] if len(list_type_permission) != 0 else []))
        return type(LSH_type) == type(RHS_type)



