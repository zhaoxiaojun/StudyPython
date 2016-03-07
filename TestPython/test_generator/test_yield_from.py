#coding=utf8

class SwitchSign(Exception):
    pass


class BreakOut(Exception):
    pass


def inner():
    coef = 1
    total = 0
    while True:
        try:
            input_val = yield total
            total = total + coef * input_val
        except SwitchSign:
            coef = -(coef)
        except BreakOut:
            return
            #return total


def outer1():
    print("Before inner(), I do this.")
    i_gen = inner()
    input_val = None
    ret_val = i_gen.send(input_val)
    while True:
        try:
            input_val = yield ret_val
            ret_val = i_gen.send(input_val)
        except StopIteration:
            break
        except Exception as err:
            try:
                ret_val = i_gen.throw(err)
            except StopIteration:
                break
    print("After inner(), I do that.")


# def outer2():    #使用yield from的方式完成outer1的功能
#     print("Before inner(), I do this.")
#     yield from inner()  #Python 3.3以上版本中支持
#     print("After inner(), I do that.")


if __name__ == '__main__':
    import code
    shell = code.InteractiveConsole(globals())
    shell.interact()
