from llvmlite import ir, binding
import re

# Create some useful types
double = ir.DoubleType()
fnty = ir.FunctionType(double, (double, double))
# Create the core module
# to create the core module, we need to parse the given llvmir, a string containing LLVM IR code. If successful, a new ModuleRef instance is returned
# You can obtain llvmir by calling str() on an llvmlite.ir.Module object
# binding.parse_assembly(llvmir, context=None)

core = ir.Module(name='__core__')
class Function():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value
        func = ir.Function(core, ir.FunctionType('''<returnType>,
                                          (<parameter type list> (self,etc))'''), name="function name")
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        a,b = func.args
        result = builder.fadd(a, b, name="res")
        builder.ret(result)
    pass
class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.value))
        return i

class Char():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        c = ir.Constant(ir.IntType(8), ord(self.value))
        return c

class String():
    def __init__(self, builder, module, values):
        self.chartype = Type.int(8)
        self.chars = [ir.Constant.int(chartype, ord(c)) for c in values]
        string = ir.Constant.array(chartype, chars)
        ptr =string.gep()
    pass
class Array():
    pass
    """
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list
    """

class ArrayElement():
    def eval(self):
        pass
    pass

class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder
        self.module = module
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i

class Sub(BinaryOp):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i

class Div(BinaryOp):
    def eval(self):
        i = self.builder.udiv(self.left.eval(), self.right.eval())
        return i

class Mul(BinaryOp):
    def eval(self):
        i = self.builder.mul(self.left.eval(), self.right.eval())
        return i
    
class Print():
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.printf, [fmt_arg, value])
