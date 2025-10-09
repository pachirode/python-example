import asyncio
import contextvars

ctx = contextvars.ContextVar('trace')
ctx.set("begin")


async def fun():
    ctx.set(ctx.get() + "|fun")
    print("ctx:", ctx.get())


async def main():
    ctx.set(ctx.get() + "|main")
    print("before call fun: ctx", ctx.get())
    await fun()
    print("after call fun: ctx", ctx.get())


print("before call main: ctx", ctx.get())
asyncio.get_event_loop().run_until_complete(main())
print("after call main: ctx", ctx.get())

# 普通方法

print("=============================")

ctx = contextvars.ContextVar("number")
ctx.set(0)


def fun1():
    ctx.set(1)
    print("fun: ctx", ctx.get())


def main():
    print("before call fun: ctx", ctx.get())
    context = contextvars.copy_context()
    context.run(fun1)
    print("after call fun: ctx", ctx.get())


main()
