# alicebot.utils


## _class_ `LinkedQueue`

基类：`Generic`[`alicebot.utils.T_Node`]

限定长度的链队列基类。


## _class_ `Condition`

基类：`object`

类似于 asyncio.Condition ，但允许在 notify() 时传递值，并由 wait() 返回。
